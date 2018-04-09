#!/usr/bin/python3

import json
import re
import requests

firstWithJudgment = 1010
lastWithJudgment = 1573

pathToJsons = "/home/mariusz/Pobrane/data/json/";


polishLetters="ĄąĆćĘęŁłŃńÓóŚśŹźŻż";



def textWithoutHTML(content):
    withoutNL = re.sub(r"-\n", "", content);
    withoutHTML = re.sub(r"<[^>]*>", "", withoutNL);
    wordList = re.findall(r"[A-Za-z" + polishLetters + r"]+", withoutHTML);
    return " ".join(wordList);

#ran partially on 2 pc
#for judgmentIndex in range(1009, 1572):
#for judgmentIndex in range(1010, 1573+1):
for judgmentIndex in reversed(range(1350, 1500)):
    print(judgmentIndex)
    stats = dict();
    with open(pathToJsons + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
        judgmentJson = json.loads(judgmentFile.read())
        for item in judgmentJson["items"]:
            if item["judgmentDate"][:4] == "2014":
                content = textWithoutHTML(item["textContent"])
                res = requests.post("http://localhost:9200", content.encode("utf-8"));
                tags = [];
                for i, line in enumerate(res.text.split("\n")):
                    parsed = re.search("\t([A-Za-z" + polishLetters + "]+\t\w+)", line)#(?::|\t)", line)
                    if parsed:
                        tags.append(parsed.group(1).replace("\t",":"))

                for i in range(1, len(tags)):
                    bigram = tags[i-1] + " " + tags[i];
                    stats[bigram] = stats.get(bigram, 0) + 1;

    with open("./bigramsStats/" + str(judgmentIndex) + ".txt", "w") as output:
        for bigram, amount in stats.items():
            output.write("{};{}\n".format(bigram, amount));

        
                        

                
                




