import random
import time
import corpus as corpuslib
corpus = corpuslib.corpus

def writer(count = 10):
    for i in range(0,count):
        cor = corpus[random.randrange(len(corpus))]
        print(cor[0])
        input()
        print(cor[1])

def typer(count = 50):
    score = 0
    num = count
    tstart = time.time()
    for i in range(0,num):
        ind = random.randrange(len(corpus))
        cor = corpus[ind]
        let = input(cor[1] + " : ")
        if let != cor[1]:
            print("incorrect: ", cor[0] )
        else:
            score += 1
    
    tend = time.time()
    dt = tend - tstart
    print("Score: ", score / num * 100)
    print("took sec per q:", dt / num)

typer()
