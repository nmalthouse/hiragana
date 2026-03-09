import sqlite3
import json
import subprocess
import random
import src.hiragana as hira
import argparse
unicode_whitespace = u'\t\n\x0b\x0c\r\x1c\x1d\x1e\x1f \x85\xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u2028\u2029\u202f\u205f\u3000'
trans = str.maketrans("", "", unicode_whitespace)
# requires mpv to be installed and in path
# How it works
# It displays the kana and english translation for a random word.
# You sound out the word first, then type.
# Hitting enter with a blank line will play the associated mp3 file to check pronunciation
# Hitting enter with a space displays the english translation
default_kana = hira.all_hiragana
default_kana = "QAZYHN17"
parser = argparse.ArgumentParser( description="Practice reading hiragana")
parser.add_argument("--count", type=int, default = 50)
parser.add_argument("--minkana", type=int, 
                    help="If specified, only drill words with atleast MINKANA kana", default=1)

parser.add_argument('--include' , type=str, default=default_kana, 
                    help="A string specifying the hiragana groups to drill, default is: " + 
                    default_kana + " To drill just words with vowels and K's do --include AK")

parser.add_argument('--jis_include', type=str, default="", help="Same idea as include, but specifies JIS layout keyboard groups to include. Qwerty keys refer to the start of the groups: QAZYHN17")
parser.add_argument('--kanji', action='store_true', help='Display Kanji' )
parser.add_argument('--sentence', action='store_true', help='Do sentences instead of word' )
parser.add_argument('--sentence-max', type=int, help='Max length of sentences to drill' , default=1000)
parser.add_argument('--mpv-args', type=str, help='pass extra args to mpv, like --speed=0.8' , default="")
parser.add_argument('--clearcreen', type=bool, help='clear screen for each entry' , default=True)
parser.add_argument('--max-index', type=int, help='cap the index', default=None )

args = parser.parse_args()

con = sqlite3.connect("anki_cards/collection.anki2")
cur = con.cursor()
res = cur.execute("SELECT flds FROM notes")

mp3map = json.load(open("anki_cards/media"))
inv_map = {v: k for k, v in mp3map.items()}

min_kana_count = args.minkana
do_all = False

allchars = ""

if len(args.jis_include) > 0:
    allchars = hira.getAggregateStringJIS(args.jis_include)
else:
    allchars = hira.getAggregateString(args.include)

sentence_list = []
vocab_list = []
count = 0
prob_count = 0

def extractSoundName(pre_name):
    sound_name = pre_name.split(':')
    if len(sound_name) != 2:
        return ""
    return sound_name[1][:-1]

# lol
def removeHtmlFromSentence(sent):
    in_tag = False
    output = ""
    for char in sent:
        if in_tag:
            if char == ">":
                in_tag = False
        else:
            if char == "<":
                in_tag = True
            else:
                output += char
    return output


for item in res:
    sections = item[0].split("\x1f")
    # 0 pkey
    # 1 is standard spelling, mix of kanji and kana 
    # 2 is kanji with ruby
    # 3 is full kana spelling
    # 4 english translation
    # 5 sound mp3, within []
    # 10 is sentence in hiragana
    # 13 is sentence mp3
    if len(sections[3]) >= min_kana_count and (do_all or all(ele in allchars for ele in sections[3])):
        count += 1
        sn = extractSoundName(sections[5])
        if len(sn) == 0:
            prob_count += 1;
            continue
        mp3_name = inv_map[sn]
        vocab_list.append({'kana': sections[3], 'mp3':mp3_name, 'english': sections[4], 'kanji': sections[1]})

    if args.sentence:
        sent = removeHtmlFromSentence(sections[10])
        if len(sent) > args.sentence_max:
            continue
        sn = extractSoundName(sections[13])
        if len(sn) == 0:
            prob_count += 1;
            continue
        sentence_list.append({
            "kana": sent,
            "mp3": inv_map[sn],
            'kanji': removeHtmlFromSentence(sections[8]),
            "english": sections[11],
            })

if args.sentence:
    print("num sentence: ", len(sentence_list), " Prob words: ", prob_count)
else:
    print("num words: ", count, " Prob words: ", prob_count)

v_list = vocab_list
if args.sentence:
    v_list = sentence_list

last_index = 0
for i in range(0, args.count):
    max_index = len(v_list)
    if args.max_index != None and args.max_index < max_index:
        max_index = args.max_index
        
    index = random.randrange(max_index)
    if len(v_list) > 1:
        while index == last_index: # prevent the same question twice in a row  
            index = random.randrange(max_index)
        last_index = index

    item = v_list[index]

    if args.clearcreen:
        print('\033[2J\033[H')
    print(item['kana'])
    if args.kanji and item["kanji"] != item['kana']:
        print(item["kanji"])

    while True:
        response = input(':')
        if response == "":
            # playsound
            subprocess.run(['mpv', args.mpv_args,'anki_cards/' + item['mp3']], capture_output = True)
        elif response in unicode_whitespace:
            print(item['english'])
        else:
            if response.translate(trans) != item['kana'].translate(trans):
                print("INCORRECT")
            else:
                break
