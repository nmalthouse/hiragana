import sqlite3
import json
import subprocess
import random
import corpus
# requires mpv to be installed and in path
# How it works
# It displays the kana and english translation for a random word.
# You sound out the word first, then type.
# Hitting enter with a blank line will play the associated mp3 file to check pronunciation

con = sqlite3.connect("anki_cards/collection.anki2")
cur = con.cursor()
res = cur.execute("SELECT flds FROM notes")

mp3map = json.load(open("anki_cards/media"))
inv_map = {v: k for k, v in mp3map.items()}

min_kana_count = 4
ex_count = 25
do_all = False

kana = corpus.new_corp
allchars = ""
for item in kana:
    allchars += item[1]

vocab_list = []
count = 0
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
        mp3_name = inv_map[sections[5].split(':')[1][:-1]]
        vocab_list.append({'kana': sections[3], 'mp3':mp3_name, 'english': sections[4]})
    #subprocess.run(['mpv', 'anki_cards/' + mp3_name], capture_output = True)
    #break

print("num words ", count)

for i in range(0, ex_count):
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
