import numpy as np

f=open("alice.txt", "r")
contents = f.read()

previous = " "
bigram  = {}
totals = {}
for i in contents:
    if (previous+i) not in bigram.keys():
        bigram[previous+i] = 0
    bigram[previous+i] += 1
    if previous not in totals.keys():
        totals[previous] = 0
    totals[previous] += 1
    previous = i

#Normalise
for (k,v) in bigram.items():
    bigram[k] = bigram[k]/totals[k[0]]

def gen():
    #Generate
    word = " "
    while True:
        choices = {k:v for k,v in list(bigram.items()) if k[0] == word[-1]}
        word += np.random.choice(list(choices.keys()), p=list(choices.values()))[1]
        if word[-1] == " ":
            break
    return word[1:]





for i in range(100):
