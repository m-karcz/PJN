#!/usr/bin/python3

import json
import sys
import pprint
import re
from os import listdir

if len(sys.argv) != 2:
    judgmentsPath = "../../Pobrane/data/json/";
else:
    judgmentsPath = sys.argv[1];

appearances = 0;

forms = "szkoda, szkodą, szkodę, szkodo, szkody, szkodzie, szkodach, szkodami, szkodom, szkód".split(", ")
formsRegex = r"\b" + r"\b|\b".join(forms) + r"\b";

def doesAppear(text):
    return re.search(formsRegex, text);
            

for judgmentIndex in range(1011, 1572):
    with open(judgmentsPath + "judgments-" + str(judgmentIndex) + ".json") as judgmentFile:
        fileText = judgmentFile.read();
        judgmentJson = json.loads(fileText);
        for judgment in judgmentJson["items"]:
            if judgment["judgmentDate"][:4] == "2014":
                if doesAppear(judgment["textContent"]):
                        appearances += 1;

print(appearances); 
