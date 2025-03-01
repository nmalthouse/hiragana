import sqlite3
import json
import subprocess
import random
import corpus
import argparse
# requires mpv to be installed and in path
# How it works
# It displays the kana and english translation for a random word.
# You sound out the word first, then type.
# Hitting enter with a blank line will play the associated mp3 file to check pronunciation
default_kana = corpus.all_hiragana
parser = argparse.ArgumentParser( description="Practice reading hiragana")
parser.add_argument("--count", type=int, default = 50)
parser.add_argument("--minkana", type=int, help="If specified, only drill words with atleast MINKANA kana", default=1)
parser.add_argument('--include' , type=str, default=default_kana, help="A string specifying the hiragana groups to drill, default is: " + default_kana + " To drill just words with vowels and K's do --include AK")

args = parser.parse_args()

con = sqlite3.connect("anki_cards/collection.anki2")
cur = con.cursor()
res = cur.execute("SELECT flds FROM notes")

mp3map = json.load(open("anki_cards/media"))
inv_map = {v: k for k, v in mp3map.items()}

min_kana_count = args.minkana
do_all = False

allchars = corpus.getAggregateString(args.include)

vocab_list = []
count = 0
prob_count = 0
for item in res:
    sections = item[0].split("\x1f")
    # 0 pkey
    # 1 is standard spelling, mix of kanji and kana 
    # 2 is kanji with ruby
    # 3 is full kana spelling
    # 4 english translation
    # 5 sound mp3, within []
    if len(sections[3]) >= min_kana_count and (do_all or all(ele in allchars for ele in sections[3])):
        count += 1
        sound_name = sections[5].split(':')
        if len(sound_name) != 2:
            prob_count += 1
            continue
        mp3_name = inv_map[sound_name[1][:-1]]
        vocab_list.append({'kana': sections[3], 'mp3':mp3_name, 'english': sections[4]})
    #subprocess.run(['mpv', 'anki_cards/' + mp3_name], capture_output = True)
    #break

print("num words: ", count, " Prob words: ", prob_count)

for i in range(0, args.count):
    item = vocab_list[random.randrange(len(vocab_list))]

    print(item['english'],item['kana'])
    while True:
        response = input(':')
        if response == "":
            # playsound
            subprocess.run(['mpv', 'anki_cards/' + item['mp3']], capture_output = True)
        else:
            if response != item['kana']:
                print("INCORRECT")
            else:
                break
