#!/usr/bin/python3

import matplotlib.pyplot as plt

with open('ranking.txt') as fp:
    frequencyRanking = [int(line.split(":")[1]) for line in fp.readlines()];

#print(frequencyRanking[I);

fig = plt.figure();

#plt.plot([y for x, y in frequencyRanking]);
plt.plot(frequencyRanking);
plt.yscale('log');
plt.xlabel("Pozycja na liście frekwencyjnej");
plt.ylabel("Ilość wystąpień");
plt.title("Zależność ilości wystąpień od pozycji na liście frekwencyjnej");
plt.xscale('log');
plt.savefig("ranking.png");
