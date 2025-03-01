import corpus
import csv
import random
import argparse

default_kana = corpus.all_hiragana
parser = argparse.ArgumentParser(
        description='drill typing hiragana words')
parser.add_argument('--include_all' , action='store_true', help='Don\'t filter out kana')
parser.add_argument('--csv' , type=str, default="vocab1.csv")
parser.add_argument('--include' , type=str, default=default_kana, help="A string specifying the hiragana groups to drill, default is: " + default_kana + " To drill just words with vowels and K's do --include AK")

parser.add_argument('--count' , type=int, default=50, help="Number to drill")
args = parser.parse_args()


do_all = args.include_all
#fname = 'study_list.csv'
fname = args.csv
kana_col = "Vocab-kana"
eng_col = "Vocab-meaning"
#fname = 'basicvc.csv'

allchars = corpus.getAggregateString(args.include)


vocab_list = []
infile = open(fname)
rd = csv.DictReader(infile)
for row in rd:
    k = row[kana_col]
    if do_all or all(ele in allchars for ele in k):
        expr = ""
        if 'expression' in row:
            expr = row['expression']
        nl = [k, row[eng_col], expr]
        vocab_list.append(nl)


def write_test(count = args.count):
    score = 0
    for i in range(0,count):
        v = vocab_list[random.randrange(len(vocab_list))]
        print(v[2],v[1], " : ", v[0])
        attempt = input()
        if attempt != v[0]:
            print("Incorrent")
        else:
            score += 1

    print("Score: ", score / count * 100)


print("num words: ", len(vocab_list))
write_test()
