#!/usr/bin/python3

import re;

existent = set();

with open("polimorfologik-2.1.txt", "r") as dictionary:
    for line in dictionary.readlines():
        existent.add(line.split(";")[1].lower());

with open("nonExistent.txt", "w") as nonExistentFile:
    with open("ranking.txt", "r") as rankingFile:
        for line in rankingFile.readlines():
            word = line.split(":")[0];
            if word not in existent:
                nonExistentFile.write(word + "\n");
