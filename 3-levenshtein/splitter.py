#!/usr/bin/python3

import json
import sys
import re

pathToJsons = "/home/mariusz/Pobrane/data/json/";

polishLetters="ĄąĆćĘęŁłŃńÓóŚśŹźŻż";

wordBank = dict();

def getWordList(content):
    withoutNL = re.sub(r"-\n", "", content);
    withoutHTML = re.sub(r"<[^>]*>", "", withoutNL);
    wordList = re.findall(r"[A-Za-z" + polishLetters + r"]+", withoutHTML);
    wordListLower = [word.lower() for word in wordList];
    return wordListLower;

def applyFileToBank(pathToFile):
    with open(pathToFile, "r") as judgmentFile:
        judgmentJson = json.loads(judgmentFile.read());
        for item in judgmentJson["items"]:
            if item["judgmentDate"][:4] == "2014":
                for word in getWordList(item["textContent"]):
                    wordBank[word] = wordBank.get(word, 0) + 1;

def wordListToRanking():
    ranking = list(wordBank.items());
    ranking.sort(key=lambda x: x[1], reverse=True);
    return ranking;

def writeRanking(ranking):
    with open("ranking.txt", "w") as rankingFile:
        for word, amount in ranking:
            rankingFile.write("{}: {}\n".format(word, amount));


for index in range(1011, 1572):
    print(index)
    applyFileToBank(pathToJsons + "judgments-" + str(index) + ".json");



#applyFileToBank(pathToFileEx);
ranking = wordListToRanking();
writeRanking(ranking);
