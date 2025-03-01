import corpus
import csv
import random


do_all = False
#fname = 'study_list.csv'
fname = 'vocab1.csv'
kana_col = "Vocab-kana"
eng_col = "Vocab-meaning"
#fname = 'basicvc.csv'
#Vocab-kana
#Vocab-meaning

kana = corpus.new_corp
allchars = ""
for item in kana:
    allchars += item[1]



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


def write_test(count = 30):
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
