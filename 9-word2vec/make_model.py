import os
import pickle
from gensim.models.word2vec import Word2Vec
from gensim.models.phrases import Phrases, Phraser
from pathlib import Path
import time

model_name = "my_model"


number_of_trigrams = 9

class sentence_iterator:
    def __init__(self):
        self.i = 0
        self.n = 1
        self.tri = self.load_tri()
        self.size = len(self.tri)

    def load_tri(self):
        print(self.n)
        with open("trigrams_{}.pickle".format(self.n), "rb") as trigrams_file:
            trigrams = pickle.load(trigrams_file)
            return trigrams

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.size:
            self.i = 0
            self.n += 1
            if self.n > number_of_trigrams:
                raise StopIteration
            else:
                self.tri = self.load_tri()
                self.size = len(self.tri)

        sentence = self.tri[self.i]
        self.i += 1
        return sentence




if Path("my_model_after_0").is_file():
    my_model = Word2Vec.load("my_model_after_0")
else:
    my_model = Word2Vec(size=300, sg=0, window=5, min_count=3, workers=4)
    my_model.build_vocab(sentence_iterator())
    my_model.save("my_model_after_0")


for i in range(1, number_of_trigrams+1):
    file_name = model_name + "_after_" + str(i)
    if Path(file_name).is_file():
        my_model = Word2Vec.load(file_name)
    else:
        with open("trigrams_{}.pickle".format(i), "rb") as trigrams_file:
            trigrams = pickle.load(trigrams_file)
            my_model.train(trigrams, total_examples=my_model.corpus_count, epochs=1)
            my_model.save(file_name)
            print("{}:\t{}".format(i, time.strftime("%X")))
