import random
import time
import corpus as corpuslib
corpus = corpuslib.new_corp

def writer(count = 10):
    for i in range(0,count):
        cor = corpus[random.randrange(len(corpus))]
        print(cor[0])
        input()
        print(cor[1])

def typer(count = 50, stlen = 1):
    score = 0
    num = count
    tstart = time.time()
    for i in range(0,num):
        key = ""
        for j in range(0,stlen):
            key += corpus[random.randrange(len(corpus))][1]

        #ind = random.randrange(len(corpus))
        #cor = corpus[ind]
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
