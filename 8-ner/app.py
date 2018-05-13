#!/usr/bin/env python3
import json
import os
import re
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import heapq
import requests
import time
import pickle

firstWithJudgment = 1010
lastWithJudgment = 1573
pathToJsons = "/home/mariusz/Pobrane/data/json/";
polishLetters="ĄąĆćĘęŁłŃńÓóŚśŹźŻż";

base_url = "http://ws.clarin-pl.eu/nlprest2/base"

lpmn = "any2txt|wcrft2|liner2({\"model\":\"n82\"})"

full_chans = dict()

full_orth_chans = dict()

def textWithoutHTML(content):
    withoutNL = re.sub(r"-\n", "", content);
    withoutHTML = re.sub(r"<[^>]*>", "", withoutNL);
#    wordList = re.findall(r"[A-Za-z,." + polishLetters + r"]+", withoutHTML);
#    return " ".join(wordList);
    return withoutHTML

def date2num(d):
    year = int(d[:4])
    month = int(d[5:7])
    day = int(d[8:10])
    return year * 10000 + month * 10 + day;

def ner(text_data):
    first_id = requests.post("{}/startTask".format(base_url), json={"lpmn": lpmn, "text": text_data}).text
    second_id = []
    def wait_until_done():
        result = requests.get("{}/getStatus/{}".format(base_url, first_id)).json()
        if(result["status"] == "DONE"):
            second_id.append(result["value"][0]["fileID"])
            return False
        else:
            time.sleep(1)
            return True

    while(wait_until_done()):
        pass

    return requests.get("{}/download{}".format(base_url, second_id[0])).text

def parse_xml(xml):
    root = ET.fromstring(xml)
    #root = ET.parse("test.xml").getroot()
    for chunk in root:
        for sentence in chunk:
            for tok in sentence:
                orth_tag = tok.findall("orth")
                if(orth_tag) :
                    orth = tok.find("orth").text
                    for tag in tok:
                        if(tag.tag == "ann"):
                            chan = tag.attrib["chan"]
                            orth_chan = (orth, chan)
                            full_chans[chan] = full_chans.get(chan, 0) + 1
                            full_orth_chans[orth_chan] = full_orth_chans.get(orth_chan, 0) + 1
                    



allJudgments = []



for judgmentIndex in range(firstWithJudgment - 2, lastWithJudgment + 2):
    print(judgmentIndex)
    path = pathToJsons + "judgments-" + str(judgmentIndex) + ".json"
    with open(path) as judgmentFile:
        judgmentJson = json.loads(judgmentFile.read())
        for i, item in enumerate(judgmentJson["items"]):
            if item["judgmentDate"][:4] == "2014":
                allJudgments.append((date2num(item["judgmentDate"]), path, i))

judgmentsToParse = heapq.nsmallest(100, allJudgments, key=lambda x: x[0])

#print(judgmentsToParse)
j = 0

for date, path, i in judgmentsToParse:
    with open(path) as judgmentFile:
        print(j)
        j += 1
        judgmentJson = json.loads(judgmentFile.read())
        xml = ner(textWithoutHTML(judgmentJson["items"][i]["textContent"]))
        parse_xml(xml)

#parse_xml(0)

#print(full_chans)
#print(full_orth_chans)

with open("full_chans.pickle", "wb") as fp:
    pickle.dump(full_chans, fp)

with open("full_orth_chans.pickle", "wb") as fp:
    pickle.dump(full_orth_chans, fp)


with open("full_chans.pickle", "rb") as fp:
    full_chans = pickle.load(fp)

with open("full_orth_chans.pickle", "rb") as fp:
    full_orth_chans = pickle.load(fp)

#print(full_chans)

def print_dict(dict_to_print, file_name):
    plt.figure()
    #labels, amounts = full_chans.items()
    labels = dict_to_print.keys()
    amounts = dict_to_print.values()
    plt.bar(range(0, len(labels)), amounts)
    plt.xticks(range(0, len(labels)), labels, rotation="vertical")
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig(file_name)

print_dict(full_chans, "full_chans.png")

reduced_chans = dict()

for label, amount in full_chans.items():
    reduced_label = "_".join(label.split("_")[0:2])
    reduced_chans[reduced_label] = reduced_chans.get(reduced_label, 0) + amount

print_dict(reduced_chans, "reduced_chans.png")

def top_n(dict_to_reduce, amount, file_name):
    #judgmentsToParse = heapq.nsmallest(100, allJudgments, key=lambda x: x[0])
    top = heapq.nlargest(amount, dict_to_reduce.items(), key=lambda x: x[1])
    with open(file_name, "w") as fp:
        fp.write("{} | {} | {}\n".format("Word", "Category", "Amount"))
        fp.write("--- | --- | ---\n")
        for info, amount in top:
            fp.write("{} | {} | {}\n".format(info[0], info[1], amount))

top_n(full_orth_chans, 100, "top100.md")

reduced_orth_chans = dict()

for label, amount in full_orth_chans.items():
    reduced_label = (label[0], "_".join(label[1].split("_")[0:2]))
    reduced_orth_chans[reduced_label] = reduced_orth_chans.get(reduced_label, 0) + amount

top_n(reduced_orth_chans, 10, "top10.md")
