#!/usr/bin/env python3

import re
import os
import math

bigrams = dict()
adjAndNouns = dict()
bigramsAmount = 0

adjAndNounTypes = ["subst", "depr", "adj", "adja", "adjp", "adjc"]
nounTypes = ["subst", "depr"]

i = 0

for filename in os.listdir("./bigramsStats/"):
    i += 1
    print(i)
    with open("./bigramsStats/" + filename) as fp:
        for line in fp.readlines():
            bigram, amountStr = line.split(";")
            amount = int(amountStr)
            bigramsAmount += amount
            first, second = bigram.split(" ")
            firstType = first.split(":")[1]
            secondType = second.split(":")[1]
            isFirst = firstType in adjAndNounTypes
            isSecond = secondType in adjAndNounTypes
            if isFirst:
                adjAndNouns[first] = adjAndNouns.get(first, 0) + amount
            if isSecond:
                adjAndNouns[second] = adjAndNouns.get(second, 0) + amount
            if isSecond and firstType in nounTypes:
                bigrams[bigram] = bigrams.get(bigram, 0) + amount

wordsAmount = bigramsAmount



def LLR(bigram, bigramAmount):
    x_word, y_word = bigram.split(" ")
    xAmount = adjAndNouns[x_word]
    yAmount = adjAndNouns[y_word]


    k_table = [bigramAmount, xAmount - bigramAmount, yAmount - bigramAmount, wordsAmount - xAmount - yAmount + bigramAmount]

    def rowSums(k):
        return [k[0]+k[1], k[2]+k[3]]

    def colSums(k):
        return [k[0]+k[2], k[1]+k[3]]

    def H(k):
        N = sum(k)
        return sum([ki/N * math.log(ki/N if ki != 0 else 1) for ki in k])

    return 2 * sum(k_table) * (H(k_table) - H(rowSums(k_table)) - H(colSums(k_table)))



top30g2 = []

for bigram, amount in bigrams.items():
    value = LLR(bigram, amount)
    if 30 == len(top30g2):
        if value > top30g2[0][1]:
            top30g2[0] = [bigram, value]
            top30g2.sort(key=lambda x: x[1])
    else:
        top30g2.append([bigram, value])
        if 30 == len(top30g2):
            top30g2.sort(key=lambda x: x[1])



with open("top30g2.txt", "w") as g2output:
    for bigram, value in reversed(top30g2):
        g2output.write("{}: {}\n".format(bigram, value))
