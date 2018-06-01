import pickle
import json

with open("rawdata.pickle", "rb") as fp:
    rawdata = pickle.load(fp)

chosen_tag = "polska"

entries = set()


i = 0
for entry in rawdata:
    text = entry["title"] + " " + entry["description"] + "\n"
    if chosen_tag in entry["tags"].replace("#","").split(" "):
        text = "__label__" + chosen_tag + " " + text
    else:
        text = "__label__no" + chosen_tag + " " + text
    entries.add(text)

print(len(entries))

with open("data.train", "w") as train_fp:
    with open("data.valid", "w") as valid_fp:
        for text in entries:
            if i % 4 == 0:
                valid_fp.write(text)
            else:
                train_fp.write(text)
            i += 1
