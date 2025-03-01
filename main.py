import sqlite3
import json
import subprocess

con = sqlite3.connect("anki_cards/collection.anki2")
cur = con.cursor()
res = cur.execute("SELECT flds FROM notes")
j = 0

mp3map = json.load(open("anki_cards/media"))
inv_map = {v: k for k, v in mp3map.items()}

for item in res:
    sections = item[0].split("\x1f")
    # 0 pkey
    # 1 is standard spelling, mix of kanji and kana 
    # 2 is kanji with ruby
    # 3 is full kana spelling
    # 4 english translation
    # 5 sound mp3, within []
    n = sections[0]
    print(n,sections[2])
    print(n,sections[3])
    mp3_name = inv_map[sections[5].split(':')[1][:-1]]
    subprocess.run(['mpv', 'anki_cards/' + mp3_name], capture_output = True)
    break
