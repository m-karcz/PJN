W tym zadaniu otrzymano bigramy bardziej odpowiadające tematyce przetwarzanych tekstów w porównaniu z poprzednim ćwiczeniem. Skrypt `make2grams.py` komunikował się z dockerem, natomiast `calcTop30.py` przetwarzał otrzymane dane z dockera. Poniżej 30 bigramów o najwyższej wartości LLR:

```
sąd:subst okręgowy:adj: 1428377.188927995
sąd:subst rejonowy:adj: 1275129.0061042411
ubezpieczenie:subst społeczny:adj: 1047695.8994299833
art:subst usta:subst: 974926.0289746065
skarb:subst państwo:subst: 968170.12442219
materiał:subst dowodowy:adj: 808544.5947427282
organ:subst rentowy:adj: 688534.6688050284
Sygn:subst akt:subst: 665192.8637390452
zeznanie:subst świadek:subst: 589851.4271724995
sąd:subst wysoki:adj: 517935.2564963659
Rzeczpospolita:subst Polski:adj: 492839.5499537357
koszt:subst proces:subst: 474911.1980251781
art:subst k:subst: 461215.343361928
ustalenie:subst faktyczny:adj: 446806.94893438526
stan:subst faktyczny:adj: 441187.8447914808
sąd:subst apelacyjny:adj: 434085.993523821
działalność:subst gospodarczy:adj: 430918.0173470503
dzień:subst grudzień:subst: 426626.3747890496
sygn:subst akt:subst: 426327.2400663793
pozbawienie:subst wolność:subst: 423414.9299872768
usta:subst ustawa:subst: 409463.7453876845
strona:subst powodowy:adj: 408591.30070902576
dzień:subst wrzesień:subst: 408551.9801571212
dzień:subst styczeń:subst: 395689.9388205055
dzień:subst październik:subst: 386412.0469416757
zastępstwo:subst procesowy:adj: 386019.2232035894
dzień:subst czerwiec:subst: 382841.0152426664
dzień:subst marzec:subst: 379933.00226754753
dzień:subst lipiec:subst: 372876.10645793367
księga:subst wieczysty:adj: 366603.1106910492
```

Zastanawiajace może być dlaczego `Sygn` zostało rozponane jako rzeczownik. Otrzymano też kilka wyników, które zostały niepoprawnie zinterpretowane jako bigram po usunięciu liczb, jak np. `dzień wrzesień` i inne sformułowania w tym stylu. 