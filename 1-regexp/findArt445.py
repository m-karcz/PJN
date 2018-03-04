#!/usr/bin/python3

import json
import sys
import re

if len(sys.argv) != 2:
    judgmentsPath = "../../Pobrane/data/json/";
else:
    judgmentsPath = sys.argv[1];

appearances = 0;

def doesAppear(reference):
    return reference["journalYear"] == 1964 and re.search("Kodeks cywilny", reference["text"]) and re.search(r"art. 445\b", reference["text"]);

for judgmentIndex in range(1011, 1572):
    print(judgmentIndex);
    with open(judgmentsPath + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
        fileText = judgmentFile.read();
        judgmentJson = json.loads(fileText);
        for judgment in judgmentJson["items"]:
            if judgment["judgmentDate"][:4] == "2014":
                for reference in judgment["referencedRegulations"]:
                    if doesAppear(reference):
                        appearances += 1;

print(appearances); 
