from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
import time
import numpy as np
import pickle


TAG = "TG"

D = 6349

max_case_amount = 1000

with open(TAG + "_IDF.pickle", "rb") as idf:
    N = len(pickle.load(idf))

case_types =["ZUS",
        "KAR",
        "GOS",
        "PIP",
        "ROD",
        "WYK",
        "KON",
        "CYW"]

chosen_case = "ZUS"

print([D, N])
X_set = np.zeros(shape=[D, N], dtype=float)

tagged_Y = []
def tagged_Y_to_values(tagged, actual_tag):
    arr = np.empty([len(tagged)], dtype=bool)
    for i, tag in enumerate(tagged):
        arr[i] = (tag == actual_tag)
    return arr;

i = 0

for case_type in case_types:
    value = 1 if case_type == chosen_case else 0
    case_amount = 0
    with open("./splitted/" + case_type + "_T.txt") as train_set:
        for file_name in train_set.readlines():
            file_name = "./vectorized/" + TAG + "/" + case_type + "/" + file_name[:-4] + "pickle"
            with open(file_name, "rb") as fp:
                compressed_vector = pickle.load(fp)
                for n in range(N):
                    X_set[i][n] = compressed_vector.get(n, 0)

                tagged_Y.append(case_type)
                i += 1
                if i % 100 == 0:
                    print(i)
                case_amount += 1
                if(case_amount > max_case_amount):
                    break;
for case_type in case_types:
    classifier = LinearSVC()
    print("START " + case_type)
    print(time.ctime())
    classifier.fit(X_set, tagged_Y_to_values(tagged_Y, case_type))
    print(time.ctime())
    with open("svc_" + TAG + "_" + case_type + ".pickle", "wb") as fp:
        pickle.dump(classifier, fp)
