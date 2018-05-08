#!/usr/bin/env python3

import WNQuery
import os
import pickle
import networkx as nx
import matplotlib.pyplot as plt
import math

nullout = open(os.devnull, "w")

def make_synonym_string(synset):
    return ",".join([syn.literal for syn in synset.synonyms])




wn = WNQuery.WNQuery("./plwordnet-3.1-visdisc.xml", nullout)

def synset_from_wnid(wnid):
    return next((wn.lookUpID(wnid, i) for i in ["n", "v", "a", "b"]), None)

def synset_from_literal_and_sense(literal, sense):
    return next((wn.lookUpSense(literal, sense, i) for i in ["n", "v", "a", "b"]), None)

def my_lea_cho(wnid_from, wnid_to):
    D = 20
    already_visited = set()
    def make_step(to_visit):
        new_to_visit = set()
        for wnid_to_visit in to_visit:
            synset = synset_from_wnid(wnid_to_visit)
            if synset:
                for wnid, relation in synset.ilrs:
                    if wnid == wnid_to:
                        return 1
                    if wnid not in already_visited:
                        new_to_visit.add(wnid)
                        already_visited.add(wnid)
        return 1 + make_step(new_to_visit)
    
    return - math.log(make_step(set([wnid_from])) / D)

def my_lea_cho_fixed(wnid_from, wnid_to):
    wnids = [wnid_from, wnid_to]
    def find_with_relations(wnid, relation_str):
        synset = synset_from_wnid(wnid)
        if synset:
            result = []
            for wnid, relation in synset.ilrs:
                if relation == relation_str:
                    result.append(wnid)
            return result
        else:
            return []

    def find_hypernyms(wnid):
        return find_with_relations(wnid, "hypernym")

    def find_hyponyms(wnid):
        return find_with_relations(wnid, "hyponym")

    hypernyms = []

    def max_taxonomy_depth(wnid):
        hyponyms = find_hyponyms(wnid)
        if hyponyms:
            return 1 + max(max_taxonomy_depth(wn) for wn in hyponyms)
        else:
            return 0;

    for i, wnid in enumerate(wnids):
        tree = [[wnid]]


        def is_in_tree(wn):
            for level in tree:
                for wn_ in level:
                    if wn_ == wn:
                        return True
            return False

        while(True):
            to_insert = []
            for last_wnid in tree[-1]:
                hyps = find_hypernyms(last_wnid)
                for hyp in hyps:
                    if not is_in_tree(hyp):
                        to_insert.append(hyp)
            if to_insert:
                tree.append(to_insert);
            else:
                break

        hypernyms.append(tree)

    
    connections = []

    for level_a, list_a in enumerate(hypernyms[0]):
        for wnid_a in list_a:
            for level_b, list_b in enumerate(hypernyms[1]):
                for wnid_b in list_b:
                    if wnid_a == wnid_b:
                        connections.append([wnid_a, level_a + level_b])

    taxonomy_depths = []
    for tree in hypernyms:
        for root in tree[-1]:
            taxonomy_depths.append(max_taxonomy_depth(root))

    D = max(taxonomy_depths)

    if connections:
        min_closest = min(connections, key=lambda x: x[1])[1]
    else:
        min_closest = max(len(hypernyms[0]), len(hypernyms[1]))
        D += 1

    return - math.log(min_closest / (2 * D))
    
    
    

print("Zad 3. \"szkoda\":")

szkodaLookup = wn.lookUpLiteral("szkoda", "n")


for result in szkodaLookup:
    print()
    print("Znaczenie: {}".format(result.definition))
    print("Synonimy: {}".format(", ".join([syn.literal for syn in result.synonyms])))


print("Zad 4. \"wypadek drogowy\":\n")

wypadekLookup = wn.lookUpLiteral("wypadek drogowy", "n")

if wypadekLookup:
    result = wypadekLookup[0]

    first = wn.lookUpRelation(result.wnid, "n", "hypernym")

    edge_labels = {}
    node_labels = {}

    G = nx.DiGraph()
    
    def find_hypernyms(wnid):
        G.add_node(wnid)
        synset = synset_from_wnid(wnid)

        node_labels[synset.wnid] = synset.wnid + "\n\n" + make_synonym_string(synset)
        rel_res = wn.lookUpRelation(synset.wnid, synset.pos, "hypernym")
        for new_wnid in rel_res:
            G.add_edge(wnid, new_wnid)
            edge_labels[(synset.wnid, new_wnid)] = "hyperonimia"
            find_hypernyms(new_wnid)
                
    find_hypernyms(result.wnid)

    plt.figure()

    lay = nx.layout.circular_layout(G)

    nx.draw_networkx_nodes(G, lay, alpha=0.0)
    nx.draw_networkx_edges(G, lay)
    nx.draw_networkx_labels(G, lay, node_labels, font_size=6)
    nx.draw_networkx_edge_labels(G, lay, edge_labels, font_size=6)

    ax = plt.gca()
    ax.set_axis_off()

    plt.savefig("zad4.png")

    print("![](zad4.png)")

print("Zad 5. wypadek:1\n")

rightWypadek = wn.lookUpSense("wypadek", 1, "n")

if rightWypadek:

    firstHyponyms = wn.lookUpRelation(rightWypadek.wnid, "n", "hyponym")

    print("Hiponimie 1 rzędu:\n")

    for hypo_wnid in firstHyponyms:
        print("{}: {}".format(hypo_wnid,make_synonym_string(synset_from_wnid(hypo_wnid))))

    print("\nZad 6. cd wypadek:1\n")

    print("Hiponimie 2 rzędu:\n")

    for hypo_wnid1 in firstHyponyms:
        for hypo_wnid2 in wn.lookUpRelation(hypo_wnid1, "n", "hyponym"):
            print("{}: {}".format(hypo_wnid2,make_synonym_string(synset_from_wnid(hypo_wnid2))))

print("\nZad 7.\n")

words_list = [[("szkoda",2), ("strata",1), ("uszczerbek",1), ("szkoda majątkowa",1),("uszczerbek na zdrowiu",1), ("krzywda",1), ("niesprawiedliwość",1), ("nieszczęście",2)],[("wypadek",1), ("wypadek komunikacyjny",1), ("kolizja",2), ("zderzenie",2), ("kolizja drogowa",1), ("katastrofa budowlana",1), ("wypadek drogowy",1)]]

for i, words in enumerate(words_list):
    plt.figure()
    G = nx.MultiDiGraph()

    node_labels = {}
    edge_labels = {}

    for word, sense in words:
        synset = synset_from_literal_and_sense(word, sense)
        if not synset:
            print("{}:{}".format(word, sense))
            
        G.add_node(synset.wnid)
        node_labels[synset.wnid] = "{}:{}".format(word, sense)
    
    for word, sense in words:
        synset = synset_from_literal_and_sense(word, sense)
        for wnid, relation in synset.ilrs:
            if wnid in node_labels:
                G.add_edge(synset.wnid, wnid)
                edge_labels[(synset.wnid, wnid)] = relation

    lay = nx.layout.circular_layout(G)

    nx.draw_networkx_nodes(G, lay, alpha=0.0)
    nx.draw_networkx_edges(G, lay)
    nx.draw_networkx_labels(G, lay, node_labels, font_size=6)
    nx.draw_networkx_edge_labels(G, lay, edge_labels, font_size=6, label_pos=0.3)

    ax = plt.gca()
    ax.set_axis_off()

    plt.savefig("zad7_{}.png".format(i+1))

    print("![](zad7_{}.png)".format(i+1))

print("Brakowało słowa \"bezkolizyjny\" w SłowoSieci.")

print("\nZad 8.\n")

to_calc = [(("szkoda",2),("wypadek",1)),(("kolizja",2),("szkoda majątkowa",1)),(("nieszczęście",2),("katastrofa budowlana",1))]

for word1, word2 in to_calc:
    syn1 = synset_from_literal_and_sense(word1[0], word1[1])
    syn2 = synset_from_literal_and_sense(word2[0], word2[1])
    
    value1 = wn.simLeaCho(syn1.wnid, syn2.wnid, "n", "hypernym", True)

    value2 = my_lea_cho_fixed(syn1.wnid, syn2.wnid)

    #my_lea_cho_fixed(syn1.wnid, syn2.wnid)

    print("WNQuery.simLeaCho({},{})={:.3f}".format(word1[0], word2[0], value1))

    print("my_lea_cho_fixed({},{})={:.3f}".format(word1[0], word2[0], value2))
