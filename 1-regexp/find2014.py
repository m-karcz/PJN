#!/usr/bin/python3

import json
import sys
import re

simplePLN = r"[0-9]+[0-9 \t\n,.]*";

valuesToReplace = {
        "tysięcy": "000",
        "tys." : "000",
        "milionów": "000000",
        "mln" : "000000",
        "miliardów": "000000000",
        "mld": "000000000",
        "bilionów": "000000000000",
        "bln": "000000000000"
        };

singleAmounts = {
        "tysiąc": "1000",
        "milion": "1000000",
        "miliard": "1000000000",
        "bilion": "1000000000000"
        };

wordsToIgnoreIfExistsHigher = ["bilionów", "miliardow", "milionów", "tysięcy"];

plnRegex = "(" + simplePLN + \
        "|" + "|".join(r"[0-9 \t\n]+" + textValue for textValue in valuesToReplace.keys()) + \
        "|" + "|".join(singleAmounts.keys()) + \
        ")";

plnRegex = plnRegex + "".join(r"(?:\d+\s" + toIgnore + r"\s)?" for toIgnore in wordsToIgnoreIfExistsHigher);
       
#plnRegex = plnRegex + r"(?:\((?:\w+\s*)+\))?";
plnRegex = plnRegex + r"(?:\(.+\))?";

plnRegex = plnRegex + "\s+(?:starych\s+)?(?:zł\w*|PLN)";

print(plnRegex)

def normalizePLN(num):
    for literal, value in valuesToReplace.items():
        num = num.replace(literal, value);
    for literal, value in singleAmounts.items():
        num = num.replace(literal, value);
    num = num.replace("tys","000");
    num = num.replace(".","");
    num = num.replace(" ","");
    num = num.replace("\n","");
    num = num.split(",")[0];
    return int(num);
    

def findPLNText(text):
    arr = [];
    for found in re.findall(plnRegex, text):
        arr.append(normalizePLN(found));
    return arr;
        

if len(sys.argv) != 2:
    judgmentsPath = "../../Pobrane/data/json/";
else:
    judgmentsPath = sys.argv[1];

money = [];

for judgmentIndex in range(1011, 1572):
    print(judgmentIndex);
    with open(judgmentsPath + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
        fileText = judgmentFile.read();
        judgmentJson = json.loads(fileText);
        for judgment in judgmentJson["items"]:
            if judgment["judgmentDate"][:4] == "2014":
               money.extend(findPLNText(judgment["textContent"]));

                
print(len(money));

with open("money2.txt", "w") as fp:
    for item in money:
        fp.write("{}\n".format(item));

