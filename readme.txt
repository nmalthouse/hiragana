Small python programs to help learn Hiragana

symb.py is the most basic start with:
python symb.py --include A # Start with learning the vowels

vocab.py drills typing words

reading.py drills words using an anki deck. An audio file can be played by hitting enter without any input
reading.py requires mpv be installed and in your path

run with --help on any of the programs to see options

Download the anki deck with:
https://ankiweb.net/shared/info/2141233552
unzip the downloaded .apkg to a folder named anki_cards inside this directory
using zip:

unzip my_deck.apkg -d anki_cards

python reading.py --minkana 4 --count 50 # Drill words with atleast 4 kana
