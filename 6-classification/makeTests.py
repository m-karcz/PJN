from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import LinearSVC
import sys
import time
import numpy as np
import pickle


TAG = sys.argv[1]


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

class Results:
    def __init__(self):
        self.positives = {False: 0, True: 0}
        self.negatives = {False: 0, True: 0}

for case_type_chosen in case_types:
    print("START " + case_type_chosen)
    print(time.ctime())
    print("classifier_" + TAG + "_" + case_type_chosen + ".pickle")
    with open("svc_" + TAG + "_" + case_type_chosen + ".pickle", "rb") as fp:
        classifier = pickle.load(fp)

    results = Results()

    for case_type in case_types:
        print(case_type_chosen + ": " + case_type)
        with open("./splitted/" + case_type + "_V.txt") as ver_set:
            for file_name in ver_set.readlines():
                file_name = "./vectorized/" + TAG + "/" + case_type + "/" + file_name[:-4] + "pickle"
                with open(file_name, "rb") as fp:
                    compressed_vector = pickle.load(fp)
                    X_predict = np.zeros(shape=[1, N], dtype=float)
                    for n in range(N):
                        X_predict[0][n] = compressed_vector.get(n, 0)


                    result = classifier.predict(X_predict)
                    if result[0]:
                        if case_type_chosen == case_type:
                            results.positives[True] += 1
                        else:
                            results.positives[False] += 1
                    else:
                        if case_type_chosen == case_type:
                            results.negatives[False] += 1
                        else:
                            results.negatives[True] += 1
    with open("results_" + TAG + "_" + case_type_chosen + ".pickle", "wb") as results_fp:
        pickle.dump(results, results_fp)

    print("Positives")
    print(results.positives)
    print("Negatives")
    print(results.negatives)



