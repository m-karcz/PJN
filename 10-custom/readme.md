# 10-custom

Jako zadanie postanowiono wybrać klasyfikację 'znalezisk' na stronie głównej portalu wykop.pl, a konkretniej przydzielanie tagu #polska.

Do wykonania tego zadania pobrano ok. 10 tysięcy znalezisk i podzielono na zbiór uczący i testujący w stosunku 3:1.

Do klasyfikacji brano string powstały ze sklejenia tytułu oraz opisu znaleziska.

Wytrenowano model i uzyskano następujące wyniki:

N       2482

P@1     0.701

R@1     0.701

Number of examples: 2482

Zatem Precision wynosi 0.701, Recall 0.701, a ponieważ F1 jest średnią harmoniczną tych dwóch, to również wynosi 0.701.