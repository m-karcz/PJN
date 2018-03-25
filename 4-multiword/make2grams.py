#!/usr/bin/python3

import json
import re

firstWithJudgment = 1010
lastWithJudgment = 1573

pathToJsons = "/home/mariusz/Pobrane/data/json/";

bigramsDict = dict()

polishLetters="ĄąĆćĘęŁłŃńÓóŚśŹźŻż";

def getBigramsList(content):
    withoutNL = re.sub(r"-\n", "", content);
    withoutHTML = re.sub(r"<[^>]*>", "", withoutNL);
    wordList = re.findall(r"[A-Za-z" + polishLetters + r"]+", withoutHTML);
    wordList = [word.lower() for word in wordList];
    bigrams = [wordList[i-1] + " " + wordList[i] for i in range(1, len(wordList))]
    return bigrams;

for judgmentIndex in range(1010, 1572):
    print(judgmentIndex)
    with open(pathToJsons + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
        judgmentJson = json.loads(judgmentFile.read())
        for item in judgmentJson["items"]:
            if item["judgmentDate"][:4] == "2014":
                for bigram in getBigramsList(item["textContent"]):
                    bigramsDict[bigram] = bigramsDict.get(bigram, 0) + 1

with open("bigramsAmount.txt", "w") as bigramsFile:
    amountSum = 0
    for bigram, amount in bigramsDict.items():
        bigramsFile.write("{}: {}\n".format(bigram, amount))
        amountSum += amount
    print("Bigrams count: %i" % amountSum)



