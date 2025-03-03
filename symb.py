import random
import time
import src.hiragana as hira
import argparse

default_kana = hira.all_hiragana
parser = argparse.ArgumentParser( description="drill individual hiragana")
parser.add_argument('--count', type=int, default=50, help="number to drill")
parser.add_argument('--len', type=int, default=1, help="number of kana per drill, default 1")
parser.add_argument('--include' , type=str, default=default_kana, help="A string specifying the hiragana groups to drill, default is: " + default_kana + " To drill just vowels and K's do --include AK")
args = parser.parse_args()
kana = hira.getAggregateList(args.include)

def typer(count = args.count, stlen = args.len):
    score = 0
    num = count
    tstart = time.time()
    for i in range(0,num):
        key = ""
        for j in range(0,stlen):
            key += kana[random.randrange(len(kana))][1]

        let = input(key + " : ")
        if let != key:
            print("incorrect: " )
        else:
            score += 1
    
    tend = time.time()
    dt = tend - tstart
    print("Score: ", score / num * 100)
    print("took sec per q:", dt / num)

typer()
