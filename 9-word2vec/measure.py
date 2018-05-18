from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

final_model = KeyedVectors.load("final_model")


print("## Zad 7")

to_find_most_similar_3 = ["sąd_najwyższy", "trybunał_konstytucyjny", "kodeks_cywilny", "kpk", "sąd_rejonowy", "szkoda", "wypadek", "kolizja", "szkoda_majątkowa", "nieszczęście", "rozwód"]

for to_find in to_find_most_similar_3:
    similars = final_model.most_similar(positive=[to_find], topn=3)
    print("#### {}:".format(to_find))
    for word, similarity in similars:
        print("\t{}: {}".format(word, similarity))

print("## Zad 8")

to_operate = [("sąd_najwyższy", "kpc", "konstytucja"), ("pasażer", "mężczyzna", "kobieta"), ("samochód", "droga", "rzeka")]

for add1, sub, add2 in to_operate:
    results = final_model.most_similar(positive=[add1, add2], negative=[sub], topn=5)
    print("#### {} - {} + {}".format(add1, sub, add2))
    for word, similarity in results:
        print("\t{}: {}".format(word, similarity))

print("## Zad 9")


# missing uszczerbek_na_zdrowiu
to_tsne = ["szkoda", "strata", "uszczerbek", "szkoda_majątkowa", "krzywda", "niesprawiedliwość", "nieszczęście"]

vectors = [final_model.get_vector(word) for word in to_tsne]

results = TSNE().fit_transform(vectors)

fig = plt.figure()

x, y = zip(*results)

plt.scatter(x, y)

for i, word in enumerate(to_tsne):
    plt.annotate(word, (x[i], y[i]))

plt.savefig("zad9.png")

print("![zad9](zad9.png)")



