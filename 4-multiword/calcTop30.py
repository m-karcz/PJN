#!/usr/bin/env python3

import heapq
import math

wordDict = dict()


#from make2grams.py
#bigramsAmount = 123433838
bigramsAmount = 148205287
logBigramsAmount = math.log(bigramsAmount)
wordsAmount = 0


with open("withOnes.txt", "r") as words:
    for line in words.readlines():
        splitted = line.strip().split(": ");
        wordDict[splitted[0]] = int(splitted[1])

for word, amount in wordDict.items():
    wordsAmount += amount

logWordsAmount = math.log(wordsAmount)

print(wordsAmount)
print(bigramsAmount)
print(2 * logWordsAmount - logBigramsAmount)

def pointWise(bigram, bigramAmount):
    splitted = bigram.split(" ")
    #logarythmic version should have lower numeric errors
    result = math.log(bigramAmount)\
        - logBigramsAmount\
        - math.log(wordDict[splitted[0]])\
        - math.log(wordDict[splitted[1]])\
        + 2 * logWordsAmount
    return result

def LLR(bigram, bigramAmount):
    x_word, y_word = bigram.split(" ")
    xAmount = wordDict[x_word]
    yAmount = wordDict[y_word]
    

    #k_table = [bigramAmount, wordsAmount - xAmount, wordsAmount - yAmount, wordsAmount - xAmount - yAmount]
    k_table = [bigramAmount, xAmount - bigramAmount, yAmount - bigramAmount, wordsAmount - xAmount - yAmount]

    def rowSums(k):
        return [k[0]+k[1], k[2]+k[3]]

    def colSums(k):
        return [k[0]+k[2], k[1]+k[3]]

    def H(k):
        N = sum(k)
        return sum([ki/N * math.log(ki/N if ki != 0 else 1) for ki in k])

    return 2 * sum(k_table) * (H(k_table) - H(rowSums(k_table)) - H(colSums(k_table)))
    


lastPercent = 0

top30pointwise = []
top30g2 = []

with open("bigramsAmount.txt", "r") as bigrams:
    i = 0
    for line in bigrams.readlines():
        bigram, amount = line.strip().split(": ");
        i += (int(amount) * 100)
        points = pointWise(bigram, int(amount))
        g2 = LLR(bigram, int(amount))
        if len(top30pointwise) < 30:
            top30pointwise.append([bigram, points])
            top30g2.append([bigram, g2])
            if len(top30pointwise) == 30:
                top30pointwise.sort(key=lambda x: x[1])
        else:
            if points > top30pointwise[0][1]:
                top30pointwise[0] = [bigram, points]
                top30pointwise.sort(key=lambda x: x[1])
            if g2 > top30g2[0][1]:
                top30g2[0] = [bigram, g2]
                top30g2.sort(key=lambda x: x[1])

        if lastPercent != int(i / bigramsAmount):
            lastPercent = int(i / bigramsAmount)
            print(lastPercent)
            '''
    top30 = []
    for line in bigrams.readlines():
        i += 100 #toremove
        if lastPercent != int(i / bigramsAmount):
            lastPercent = int(i / bigramsAmount)
            print(lastPercent) #toremove
        bigram, amount = line.strip().split(": ")
        if len(top30) < 30:
            top30.append([splitted[0], pointWise(bigram, int(amount))])
            if len(top30) == 30:
                top30.sort(key=lambda x: x[1])
        else:
            pointWiseUpperBound = math.log(int(amount))\
                - logBigramsAmount\
                + 2 * logWordsAmount
            if pointWiseUpperBound > top30[0][1]:
                words = bigram.split(" ")
                pointWiseUpperBound -= math.log(wordDict[words[0]])
                if pointWiseUpperBound > top30[0][1]:
                    pointWiseUpperBound -= math.log(wordDict[words[1]])
                    if pointWiseUpperBound > top30[0][1]:
                        top30[0] = [bigram, pointWiseUpperBound]
                        top30.sort(key=lambda x: x[1])'''
                
            



#pointwiseBigrams.sort(key=lambda x: x[1], reverse=True)

with open("top30pointwise.txt", "w") as pointwiseOutput:
    for bigram, value in reversed(top30pointwise):#heapq.nlargest(pontwiseBigrams, key=lambda x: x[1]):
        pointwiseOutput.write("{}: {}\n".format(bigram, value))

with open("top30g2.txt", "w") as g2output:
    for bigram, value in reversed(top30g2):
        g2output.write("{}: {}\n".format(bigram, value))
