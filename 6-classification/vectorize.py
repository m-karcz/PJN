import os
import os.path
import pickle
import math

case_types =["ZUS",
        "KAR",
        "GOS",
        "PIP",
        "ROD",
        "WYK",
        "KON",
        "CYW"]

path_to_parsed = "./parsed/"
path_to_vectors = "./vectorized/"

lower_bound_amount = 150
max_case_amount = 1000




N = 0
def make_vectors(tag_type):
    global N
    N = 0

    chosen_files = []

    def iterate_over_case(case_type, callback):
        folder_path = path_to_parsed + tag_type + "/" + case_type + "/";
        for _,_,file_names in os.walk(folder_path):
            for file_name in file_names:
                with open(folder_path + file_name) as fp:
                    callback(case_type, file_name, fp)

    def iterate_over_case_limited(case_type, callback):
        folder_path = path_to_parsed + tag_type + "/" + case_type + "/";
        case_amount = 0
        with open("./splitted/" + case_type + "_T.txt") as train_data:
            for file_name in train_data.readlines():
                with open(folder_path + file_name.strip()) as fp:
                    callback(case_type, file_name, fp)
                case_amount += 1
                if case_amount > max_case_amount:
                    break

    def iterate_over_all_limited(callback):
        for case_type in case_types:
            iterate_over_case_limited(case_type, callback)

    def iterate_over_all(callback):
        for case_type in case_types:
            iterate_over_case(case_type, callback)

    IDF_filename = tag_type + "_IDF.pickle"

    if os.path.isfile(IDF_filename):
        with open(IDF_filename, "rb") as idf_fp:
            idf = pickle.load(idf_fp)
    else:
        """
        cases_dict = dict()
        for case_type in case_types:
            cases_dict[case_type] = dict()
        """

        words_dict = dict()
        words_amount = dict()


        def populate_dict(case_type, file_name, fp):
            global N
            N += 1
            chosen_files.append(file_name)
            for line in fp.readlines():
                word, amount = line.split(";")

                #case_dict = cases_dict[case_type]

                #actual_state = case_dict.get(word, [0, 0])

                #case_dict[word] = [actual_state[0] + 1, actual_state[1] + int(amount)]
                
                words_dict[word] = words_dict.get(word, 0) + 1
                words_amount[word] = words_amount.get(word, 0) + int(amount)

        """

        def total_len():
            return sum([len(case_dict) for case_type, case_dict in cases_dict.items()])

        init_lens = dict()

        minimal_amounts = dict()


        for case_type, case_dict in cases_dict.items():
            init_lens[case_type] = len(case_dict)
            minimal_amounts[case_type] = 1

        percentage = 0.99

        while True:
            for case_type, case_dict in cases_dict.items():
                while len(case_dict) / init_lens[case_type] > percentage:
                    words_to_remove = []
                    minimal_amount = minimal_amounts[case_type]
                    for word, [documents, amount] in case_dict.items():
                        if amount < minimal_amount:
                            words_to_remove.append(word)
                    for word in words_to_remove:
                        case_dict.pop(word, None)
                    minimal_amounts[case_type] += 1
            print(percentage)
            tot_len = total_len()
            print(tot_len)
            if tot_len < 10000:
                break
            percentage -= 0.01



        """



        iterate_over_all_limited(populate_dict)

        #word_amount = {word, amount

        words_dict = {word: documents for word, documents in words_dict.items() if words_amount[word] > lower_bound_amount}

        """
        for i in range(0,20):
            k = None
            v = -1
            for word, amount in words_amount.items():
                if amount > v:
                    k = word
                    v = amount
            words_amount.pop(k)
            words_dict.pop(k)
        """
        """
        while(True):
            words_amount = {word: amount for word, amount in words_amount.items() if amount >= lower_bound_amount}
            am = len(words_amount)
            print("{}: {}".format(lower_bound_amount, am))
            lower_bound_amount += 1
            if am < 10000:
                break
        words_dict = {word: amount for word, amount in words_dict.items() if word in words_amount}
        """

        logN = math.log(N)

        words_sorted_tuple = sorted(words_dict.items(),key=lambda x: x[0])

        words_dict.clear()

        idf = [[pair[0], (logN - math.log(pair[1]))] for pair in words_sorted_tuple]
        with open(IDF_filename, "wb") as idf_fp:
            pickle.dump(idf, idf_fp)

    print("IDF length: " + str(len(idf)))
    print("files: " + str(N))
    
    def file_entry_to_dict_entry(entry):
        splitted = entry.split(";")
        return [splitted[0], int(splitted[1])]

    def make_vectors(case_type, file_name, fp):
        words = dict(file_entry_to_dict_entry(line) for line in fp.readlines())
        n = sum(words.values())

        vector = [words.get(word, 0) / n * idf_val for word, idf_val in idf]

        compressed_vector = {i: tfidf for i, tfidf in enumerate(vector) if tfidf != 0}
        with open(path_to_vectors + tag_type + "/" + case_type + "/" + file_name[:-4] + ".pickle", "wb") as pckl:
            pickle.dump(compressed_vector, pckl)

    iterate_over_all(make_vectors)

        

make_vectors("NT")
make_vectors("TG")
