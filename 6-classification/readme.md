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
ZUS | 0.999 | 0.688 | 0.815 | 1000
KAR | 0.998 | 0.496 | 0.663 | 1000
GOS | 0.793 | 0.035 | 0.067 | 1000
PIP | 0.896 | 0.151 | 0.258 | 1000
ROD | 0.644 | 0.453 | 0.532 | 595
WYK | 0.691 | 0.558 | 0.617 | 690
KON | 0.900 | 0.286 | 0.434 | 505
CYW | 0.884 | 0.007 | 0.014 | 1000
Micro-average | 0.851 | 0.334 | 0.425 |  
Macro-average | 0.966 | 0.262 | 0.412 |  


#### Zbiór otagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.998 | 0.768 | 0.868 | 1000
KAR | 0.997 | 0.605 | 0.753 | 1000
GOS | 0.724 | 0.096 | 0.169 | 1000
PIP | 0.882 | 0.223 | 0.356 | 1000
ROD | 0.614 | 0.601 | 0.608 | 595
WYK | 0.678 | 0.686 | 0.682 | 690
KON | 0.846 | 0.611 | 0.710 | 505
CYW | 0.949 | 0.041 | 0.078 | 1000
Micro-average | 0.836 | 0.454 | 0.528 |  
Macro-average | 0.955 | 0.330 | 0.491 |  

Zbiór tagowany w porównaniu do zbioru nietagowanego uzyskał minimalnie gorszy wskaźnik Precision, jednak znacząco wzrosła wartość Recall, a co za tym idzie wzrósł także wskaźnik F1.

### Zadanie z bardziej zredukowanym zbiorem

Postanowiono jeszcze bardziej zredukować zbiór - obcinając wyrazy, które występują mniej niż 25 razy i mniej niż 100 razy.

### > 25

#### Zbiór nieotagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.999 | 0.688 | 0.815 | 1000
KAR | 0.998 | 0.496 | 0.663 | 1000
GOS | 0.793 | 0.035 | 0.067 | 1000
PIP | 0.895 | 0.149 | 0.256 | 1000
ROD | 0.644 | 0.453 | 0.532 | 595
WYK | 0.676 | 0.558 | 0.611 | 690
KON | 0.900 | 0.286 | 0.434 | 505
CYW | 0.881 | 0.007 | 0.013 | 1000
Micro-average | 0.848 | 0.334 | 0.424 |  
Macro-average | 0.966 | 0.262 | 0.412 |  


#### Zbiór otagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.998 | 0.768 | 0.868 | 1000
KAR | 0.997 | 0.605 | 0.753 | 1000
GOS | 0.727 | 0.097 | 0.172 | 1000
PIP | 0.882 | 0.223 | 0.356 | 1000
ROD | 0.614 | 0.601 | 0.608 | 595
WYK | 0.678 | 0.686 | 0.682 | 690
KON | 0.848 | 0.619 | 0.716 | 505
CYW | 0.948 | 0.040 | 0.077 | 1000
Micro-average | 0.837 | 0.455 | 0.529 |  
Macro-average | 0.955 | 0.330 | 0.490 |  

### > 150

#### Zbiór nieotagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.999 | 0.678 | 0.808 | 1000
KAR | 0.998 | 0.487 | 0.655 | 1000
GOS | 0.750 | 0.027 | 0.053 | 1000
PIP | 0.884 | 0.133 | 0.232 | 1000
ROD | 0.634 | 0.432 | 0.514 | 595
WYK | 0.664 | 0.529 | 0.589 | 690
KON | 0.892 | 0.262 | 0.405 | 505
CYW | 0.867 | 0.005 | 0.009 | 1000
Micro-average | 0.836 | 0.319 | 0.408 |  
Macro-average | 0.965 | 0.255 | 0.403 |  

#### Zbiór tagowany

Case | Precision | Recall | F1 | Train set size
--- | --- | --- | --- | ---
ZUS | 0.998 | 0.769 | 0.869 | 1000
KAR | 0.997 | 0.604 | 0.752 | 1000
GOS | 0.714 | 0.091 | 0.162 | 1000
PIP | 0.887 | 0.221 | 0.354 | 1000
ROD | 0.615 | 0.595 | 0.605 | 595
WYK | 0.672 | 0.680 | 0.676 | 690
KON | 0.844 | 0.603 | 0.704 | 505
CYW | 0.947 | 0.039 | 0.075 | 1000
Micro-average | 0.835 | 0.450 | 0.525 |  
Macro-average | 0.955 | 0.329 | 0.489 |  

