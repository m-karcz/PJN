import os
import math

path = "./parsed/NT/"

case_types =["ZUS",
        "KAR",
        "GOS",
        "PIP",
        "ROD",
        "WYK",
        "KON",
        "CYW"]

case_amounts = {
        "CYW": 22013,
        "GOS": 2635,
        "KAR": 10729,
        "KON": 505,
        "PIP": 2280,
        "ROD": 595,
        "WYK": 690,
        "ZUS": 8503
        }

total_amount = sum(case_amounts.values())

take_every_n = math.ceil(total_amount / 7000)

print(take_every_n)


N = 0
for case_type in case_types:
    with open("./splitted/" + case_type + "_T.txt", "w") as training:
        with open("./splitted/" + case_type + "_V.txt", "w") as validating:
            i = 0
            for _, _, file_names in os.walk(path + case_type + "/"):
                for file_name in file_names:
                    N += 1
                    if(N % take_every_n == 0):
                        i += 1
                        if i % 4 == 0:
                            validating.write(file_name + "\n")
                        else:
                            training.write(file_name + "\n")
                                
