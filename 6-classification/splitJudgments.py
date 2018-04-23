import os

path = "./parsed/NT/"

case_types =["ZUS",
        "KAR",
        "GOS",
        "PIP",
        "ROD",
        "WYK",
        "KON",
        "CYW"]

for case_type in case_types:
    with open("./splitted/" + case_type + "_T.txt", "w") as training:
        with open("./splitted/" + case_type + "_V.txt", "w") as validating:
            i = 0
            for _, _, file_names in os.walk(path + case_type + "/"):
                for file_name in file_names:
                    i += 1
                    if i % 4 == 0:
                        validating.write(file_name + "\n")
                    else:
                        training.write(file_name + "\n")
                            
