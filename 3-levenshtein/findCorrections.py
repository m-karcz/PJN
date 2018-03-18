#!/usr/bin/env python3

import string;

allletters = string.ascii_lowercase + "ąćęłńóśźż";

def generateOneFurther(word):
    generated = [];
    for i in range(0, len(word)):
        #remove
        generated.append(word[:i] + word[(i+1):]);
        for letter in allletters:
            #substitute
            generated.append(str(word[:i]) + letter + str(word[(i+1):]));
            #add
            generated.append(str(word[:i]) + letter + str(word[i:]));
    #also add
    for letter in allletters:
        generated.append(str(word) + letter);
    return generated;


ranking = dict();
polimorfologik = set();

with open("ranking.txt", "r") as rankingFile: 
    for line in rankingFile.readlines():
        splitted = line.split(": ");
        ranking[splitted[0]] = int(splitted[1]);

with open("polimorfologik-2.1.txt", "r") as dictionary:
    for line in dictionary.readlines():
        polimorfologik.add(line.split(";")[1].lower());

with open("30words.txt", "r") as words:
    wordsToFix = [word.strip() for word in words.readlines()];

with open("fixes.txt", "w") as fixFile:
    for word in wordsToFix:
        winner = None;
        when = None;
        candidates1away = generateOneFurther(word);
        candidates = [candidate for candidate in candidates1away if str(candidate) in polimorfologik];
        if candidates:
            winner = max(candidates, key=lambda cand: ranking.get(cand, 0))
            when = 1;
        else:
            candidates2away = [];
            for cand in candidates1away:
                candidates2away.extend(generateOneFurther(cand));
            candidates = [candidate for candidate in candidates2away if str(candidate) in polimorfologik];
            if candidates:
                winner = max(candidates, key=lambda cand: ranking.get(cand, 0))
                when = 2;
        result = word + " >>> " + (winner + " in distance" + str(when) if winner else "???")
        print(result);
        fixFile.write(result + "\n");


