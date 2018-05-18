import os
import json

#firstWithJudgment = 1010
#lastWithJudgment = 1573
firstWithJudgment = 1100
lastWithJudgment = 1500

pathToJsons = "/home/mariusz/Pobrane/data/json/"

with open("fileList.txt", "w") as listFile:
    for judgmentIndex in range(firstWithJudgment - 1, lastWithJudgment + 1):
        print(judgmentIndex)
        with open(pathToJsons + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
            judgmentJson = json.loads(judgmentFile.read())
            for itemIndex, item in enumerate(judgmentJson["items"]):
                if item["judgmentDate"][:4] == "2014":
                    fileName = "content/content_{}_{}.txt".format(judgmentIndex, itemIndex)
                    listFile.write(fileName)
                    listFile.write("\n")
                    with open(fileName, "w") as contentFile:
                        contentFile.write(item["textContent"])
