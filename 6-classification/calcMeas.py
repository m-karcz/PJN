import numpy as np
import pickle
from statistics import mean


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

case_amount = {
        "ZUS": 1000,
        "KAR": 1000,
        "GOS": 1000,
        "PIP": 1000,
        "ROD": 595,
        "WYK": 690,
        "KON": 505,
        "CYW": 1000
        }


class Results:
    def __init__(self):
        self.positives = {False: 0, True: 0}
        self.negatives = {False: 0, True: 0}

class BetterResult:
    def __init__(self, old):
        self.TP = old.positives[True]
        self.FP = old.positives[False]
        self.TN = old.negatives[True]
        self.FN = old.negatives[False]


for TAG in ["TG", "NT"]:
    def PRE(res):
        num = sum([r.TP for r in res])
        den = sum([r.TP + r.FP for r in res])
        return num / den
    
    def REC(res):
        num = sum([r.TP for r in res])
        den = sum([r.TP + r.FN for r in res])
        return num / den

    def F1(res):
        pre = PRE(res)
        rec = REC(res)
        return 2 * (pre * rec) / (pre + rec)

    
    with open(TAG + "_results.md", "w") as res_fp:
        results = dict()
        for case_type in case_types:
            with open("results_" + TAG + "_" + case_type + ".pickle", "rb") as fp:
                temp_res = pickle.load(fp)
                results[case_type] = BetterResult(temp_res)
        res_fp.write("Case | Precision | Recall | F1 | Train set size\n")
        res_fp.write("--- | --- | --- | --- | ---\n")
        template_tab_line = "{} | {:0.3f} | {:0.3f} | {:0.3f} | {}\n"
        pre_arr = []
        rec_arr = []
        f1_arr = []
        for case, res in results.items():
            pre = PRE([res])
            rec = REC([res])
            f1 = F1([res])
            pre_arr.append(pre)
            rec_arr.append(rec)
            f1_arr.append(f1)
            res_fp.write(template_tab_line.format(case, pre, rec, f1, case_amount[case]))

        res_fp.write(template_tab_line.format("Micro-average", mean(pre_arr), mean(rec_arr), mean(f1_arr), " "))
        res_fp.write(template_tab_line.format("Macro-average", PRE(results.values()), REC(results.values()), F1(results.values()), " "))
