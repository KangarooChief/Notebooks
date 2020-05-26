import numpy as np
import mmap

f=open("alice.txt", "r")
contents = f.read()
contents = contents.replace(" ", "  ")


previous = "  "
trigram  = {}
totals = {}
for i in contents:
    if (previous+i) not in trigram.keys():
        trigram[previous+i] = 0
    trigram[previous+i] += 1
    if previous not in totals.keys():
        totals[previous] = 0
    totals[previous] += 1
    previous = previous[1] + i

#Normalise
for (k,v) in trigram.items():
    trigram[k] = trigram[k]/totals[k[0:2]]


def gen():
    word = "  "
    while True:
        choices = {k:v for k,v in list(trigram.items()) if k[0:2] == word[-2:]}
        word += np.random.choice(list(choices.keys()), p=list(choices.values()))[2]
        if word[-1] == " ":
            break
    return word[2:]


for i in range(10):
    word = gen()
    print(word)
    with open('words.txt', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(word.encode('UTF-8')) != -1:
            print('true')
