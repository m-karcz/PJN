import os
import pickle
from gensim.models.word2vec import Word2Vec
from gensim.models.phrases import Phrases, Phraser
from pathlib import Path


def prepareSentences(sentences):
    print("a")
    bigram = Phrases(sentences)
    print("b")
    trigram = Phrases(bigram[sentences])
    print("c")
    return trigram[sentences]


with open("dataList.txt") as data_list:
    to_learn = data_list.readlines()

sentences_to_parse = []


i = 0
N = 0

for index in range(0, len(to_learn)):
    file_name_to_learn = to_learn[index].strip()
    i += 1
    with open(file_name_to_learn) as file_to_learn:
        sentences = [sentence.strip().split(" ") for sentence in file_to_learn.readlines()]
        for sentence in sentences:
            sentences_to_parse.append(sentence)
    if(i % 5000 == 0):
        print(i)
        N = N + 1
        trigrams = prepareSentences(sentences_to_parse)
        with open("trigrams_{}.pickle".format(N), "wb") as fp:
            pickle.dump(trigrams, fp)
        sentences_to_parse = []

N = N + 1
trigrams = prepareSentences(sentences_to_parse)
with open("trigrams_{}.pickle".format(N), "wb") as fp:
    pickle.dump(trigrams, fp)
sentences_to_parse = []

