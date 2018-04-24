## Zadanie podstawowe

Aby umożliwić w ogóle wykonanie zadania poczyniono 2 zabiegi:

- Do zbioru uczącego wzięto maksymalnie po 1000 orzeczeń każdego rodzaju.
- Usunięto ze zbioru wszystkie wyrazy, które występowały rzadziej niż 5 razy.

Dopiero tak ograniczony zbiór mógł zmieścić się w całości w RAMie.

Wykorzystano następujące skrypty:

- *prepareVecs.py* do uzyskania słowników 'słowo: ilość' dla każdego z orzeczeń
- *splitJudgments.py* do podziału orzeczeń na zbiór uczący i testowy
- *vectorize.py* do przygotowania wektorów wagowanych TF-IDF
- *trainTest.py* do wytrenowania klasyfikatorów
- *makeTests.py* do wykonania faktycznych testów
- *calcMeas.py* do przedstawienia wyników

Poniżej przedstawiono wyniki:

#### Zbiór nieotagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.997 | 0.987 | 0.992 | 911
KAR | 0.975 | 0.911 | 0.942 | 1150
GOS | 0.795 | 0.745 | 0.769 | 282
PIP | 0.946 | 0.654 | 0.774 | 245
ROD | 0.864 | 0.905 | 0.884 | 64
WYK | 1.000 | 0.625 | 0.769 | 75
KON | 0.833 | 0.833 | 0.833 | 54
CYW | 0.974 | 0.935 | 0.954 | 2359
Micro-average | 0.923 | 0.824 | 0.865 |  
Macro-average | 0.965 | 0.909 | 0.936 |  



#### Zbiór otagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.993 | 0.983 | 0.988 | 911
KAR | 0.972 | 0.903 | 0.936 | 1150
GOS | 0.854 | 0.372 | 0.519 | 282
PIP | 0.907 | 0.605 | 0.726 | 245
ROD | 0.923 | 0.571 | 0.706 | 64
WYK | 0.875 | 0.583 | 0.700 | 75
KON | 0.789 | 0.833 | 0.811 | 54
CYW | 0.881 | 0.949 | 0.914 | 2359
Micro-average | 0.899 | 0.725 | 0.787 |  
Macro-average | 0.920 | 0.886 | 0.903 |  

Wynik jest zadziwiający, ale zbiór nieotagowany ma lepsze wyniki niż tagowany.

### Zadanie z bardziej zredukowanym zbiorem

Postanowiono jeszcze bardziej zredukować zbiór - obcinając wyrazy, które występują mniej niż 25 razy i mniej niż 100 razy.

### > 25

#### Zbiór nieotagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.987 | 0.967 | 0.977 | 911
KAR | 0.975 | 0.903 | 0.938 | 1150
GOS | 0.803 | 0.606 | 0.691 | 282
PIP | 0.971 | 0.420 | 0.586 | 245
ROD | 0.864 | 0.905 | 0.884 | 64
WYK | 1.000 | 0.583 | 0.737 | 75
KON | 0.833 | 0.833 | 0.833 | 54
CYW | 0.982 | 0.908 | 0.944 | 2359
Micro-average | 0.927 | 0.766 | 0.824 |  
Macro-average | 0.969 | 0.873 | 0.918 |  


#### Zbiór otagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.993 | 0.983 | 0.988 | 911
KAR | 0.972 | 0.903 | 0.936 | 1150
GOS | 0.854 | 0.372 | 0.519 | 282
PIP | 0.909 | 0.617 | 0.735 | 245
ROD | 0.923 | 0.571 | 0.706 | 64
WYK | 0.875 | 0.583 | 0.700 | 75
KON | 0.789 | 0.833 | 0.811 | 54
CYW | 0.881 | 0.949 | 0.914 | 2359
Micro-average | 0.900 | 0.727 | 0.789 |  
Macro-average | 0.920 | 0.887 | 0.903 |  

### > 150

#### Zbiór nieotagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.987 | 0.967 | 0.977 | 911
KAR | 0.975 | 0.903 | 0.938 | 1150
GOS | 0.800 | 0.596 | 0.683 | 282
PIP | 0.971 | 0.420 | 0.586 | 245
ROD | 0.864 | 0.905 | 0.884 | 64
WYK | 1.000 | 0.583 | 0.737 | 75
KON | 0.833 | 0.833 | 0.833 | 54
CYW | 0.982 | 0.910 | 0.945 | 2359
Micro-average | 0.926 | 0.765 | 0.823 |  
Macro-average | 0.969 | 0.873 | 0.918 |  

#### Zbiór tagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.993 | 0.983 | 0.988 | 911
KAR | 0.972 | 0.903 | 0.936 | 1150
GOS | 0.854 | 0.372 | 0.519 | 282
PIP | 0.909 | 0.617 | 0.735 | 245
ROD | 0.923 | 0.571 | 0.706 | 64
WYK | 0.875 | 0.583 | 0.700 | 75
KON | 0.789 | 0.833 | 0.811 | 54
CYW | 0.881 | 0.949 | 0.914 | 2359
Micro-average | 0.900 | 0.727 | 0.789 |  
Macro-average | 0.920 | 0.887 | 0.903 |  
