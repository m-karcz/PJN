Do zadania wykorzystano wyniki z poprzedniego zadania - nie usuniętego z nich jednoliterowych słów, więc nie była potrzebna ponowna ekstracja unigramów.

Skrypt *make2grams.py* dokonuje ekstracji bigramów do pliku wraz z liczbą ich wystąpień - *bigramsAmount.txt*.

Następnie skrypt *calcTop30.py* wyznacza po 30 bigramów o największym wskaźniku punktowej informacji wzajemnej i LLR. Poniżej przedstawiono wyniki:

Punktowa informacja wzajemna:

```
popuszczał cumy: 18.814866844465133
umkw toruniuwraz: 18.814866844465133
great britain: 18.814866844465133
sound intensity: 18.814866844465133
akademiakompetencji bcl: 18.814866844465133
zrodlowe probkidxj: 18.814866844465133
chelm bodot: 18.814866844465133
jednoelementowej przeziernej: 18.814866844465133
romanem trybusem: 18.814866844465133
beteiligungs gesselschaft: 18.814866844465133
darnnrim ernergens: 18.814866844465133
modelarsko rzeźbiarskiego: 18.814866844465133
przyślę żegnam: 18.814866844465133
sprowadzaę siź: 18.814866844465133
następnikowi presumpcji: 18.814866844465133
zagmatwaną zawikłaną: 18.814866844465133
wiecka jelińska: 18.814866844465133
wewnątrznabłonkowe nowotworzenie: 18.814866844465133
nakładową złożową: 18.814866844465133
unikoru cynkoru: 18.814866844465133
biskupem diecezjalnym: 18.814866844465133
faszystowskim gadżetom: 18.814866844465133
miękkotkankowy hypoechogenny: 18.814866844465133
cautio damni: 18.814866844465133
damni infecti: 18.814866844465133
ścieżkową anodę: 18.814866844465133
amorficznym półprzewodniku: 18.814866844465133
przysłon tabara: 18.814866844465133
siateczkowo smużkowate: 18.814866844465133
kartelowi cementowemu: 18.814866844465133

```

LLR:

```
z dnia: 3814944.0465587424
art k: 3374195.2400787966
na podstawie: 2161287.7114062556
k p: 2056643.9818356917
sąd okręgowy: 1989192.0808359873
art ust: 1938237.8927289634
p c: 1681662.3915095015
sąd rejonowy: 1446982.064067685
ubezpieczeń społecznych: 1439959.10130146
na rzecz: 1398872.504491262
pozbawienia wolności: 1258564.1918440394
w sprawie: 1198274.599436261
zgodnie z: 1196518.0080749802
kwotę zł: 1190376.6290608498
dz u: 1155956.3613417938
zw z: 1092890.993443757
podstawie art: 1007474.871725173
k c: 964854.8016161785
w tym: 962142.2071919221
w zw: 927039.9045489867
nr poz: 923040.8118674569
sądu okręgowego: 899057.797845923
sądu najwyższego: 890778.8642933861
materiału dowodowego: 813498.7851929881
związku z: 810139.2620508767
rzeczypospolitej polskiej: 792611.9550924569
skarbu państwa: 761527.372891858
stycznia r: 743746.4666323201
w związku: 731408.4849811407
art kk: 729313.3901882924
```

Dla punktowej informacji wzajemnej wzór
log(P(x->y)/(P(x)P(y))) można rozwinąć w dodawanie i odejmowanie logarytmów. Otrzymujemy z tego wyrażenie log(n(x->y)) - log(B) - log(n(x)) - log(n(y)) + 2log(N), gdzie B to liczba wszystkich bigramów, a N to liczba wszystkich unigramów. -log(B)+2log(N) jest stałe, zmienne jest jedynie wyrażenie log(n(x->y))-log(n(x))-log(n(y)). Ponieważ n(x->y) < n(x)+n(y), przyjmuje ono minimalną wartość dla n(x->y)=n(x)=n(y)=1. Zatem 30 bigramów o największej wartości to wyrażenia, które występują tylko raz i słowa je tworzące również występują tylko raz.

Natomiast LLR daje wyniki bardziej przewidywalne - jednak usunięcie liczb nieco wypaczyło wyniki, np. *kwotę zł* nie występuje w tekście jako bigram, lecz jest przedzielone faktyczną kwotą.