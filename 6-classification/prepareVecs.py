#!/usr/bin/python3

import json
import re
import requests

#firstWithJudgment = 1010
firstWithJudgment = 1430
lastWithJudgment = 1573

pathToJsons = "/home/mariusz/Pobrane/data/json/"

polishLetters="ĄąĆćĘęŁłŃńÓóŚśŹźŻż"

case2type =[["A?U.*", "ZUS"],
        ["A?K.*", "KAR"],
        ["G.*", "GOS"],
        ["A?P.*", "PIP"],
        ["R.*", "ROD"],
        ["W.*", "WYK"],
        ["Am.*", "KON"],
        ["A?C.*", "CYW"]]

def getCaseType(item):
    case = item["courtCases"][0]["caseNumber"]
    matching = [typ for reg, typ in case2type if re.search(reg,case)]
    if any(matching):
        return matching[0]
    else:
        return "NOP"




def textWithoutHTML(content):
    withoutNL = re.sub(r"-\n", "", content);
    withoutHTML = re.sub(r"<[^>]*>", "", withoutNL);
    wordList = re.findall(r"[A-Za-z" + polishLetters + r"]+", withoutHTML);
    return wordList;

def parseFromDocker(response):
    parsed = []
    for i, line in enumerate(response.text.split("\n")):
        tagged = re.search("\t([A-Za-z" + polishLetters + "]+\t\w+)", line)
        if tagged:
            parsed.append(tagged.group(1).replace("\t",":"));
    return parsed;

def countWords(words):
    result = dict()
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result;

def saveWords(countedWords, fileName):
    with open("parsed/"+fileName, "w") as fp:
        for word,amount in countedWords.items():
            fp.write("{};{}\n".format(word,amount))

def afterUzasadnienie(content):
    while any(content) and content.pop(0).upper() != "UZASADNIENIE":
        pass
    return content
    
    

for judgmentIndex in range(firstWithJudgment - 1, lastWithJudgment + 1):
    with open(pathToJsons + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
        judgmentJson = json.loads(judgmentFile.read())
        for itemIndex, item in enumerate(judgmentJson["items"]):
            if item["judgmentDate"][:4] == "2014" and (item["courtType"] == "COMMON" or item["courtType"] == "SUPREME"):
                print("{}:{}".format(judgmentIndex,itemIndex))

                caseType = getCaseType(item)

                fileName = "{}/{}_{}.txt".format(caseType, judgmentIndex, itemIndex)
                
                content = textWithoutHTML(item["textContent"])

                content = afterUzasadnienie(content)

                if not any(content):
                    continue

                saveWords(countWords(content), "NT/" + fileName)
                
                contentJoined = " ".join(content)

                tagged = parseFromDocker(requests.post("http://localhost:9200", contentJoined.encode("utf-8")))

                saveWords(countWords(tagged), "TG/" + fileName)
