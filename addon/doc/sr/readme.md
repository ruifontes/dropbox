# dropbox #
[[!meta title="dropbox"]]

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak dodaje prečicu za izgovor dropbox statusa, verzije ili
otvaranje menija u sistemskoj traci.  takođe možete menjati kartice u
podešavanjima sa Ctrl+tab / Ctrl+Shift+Tab i Ctrl+PageUp/Down.  Kao
zaključak, možete aktivirati dugme otkaži sa tasterom escape.

* Prečica: NVDA+alt+d
* Ctrl+Alt+T izgovara trenutnu karticu.

## Poznati problemi ##

* Ukoliko menjate kartice u podešavanjima, kada zatvorite prozor za podešavanja, NVDA neće znati da prozor više ne postoji.
To je poznat NVDA problem i ne može biti popravljen.


## Promene u 4.0 ##

* Pomoć za dodatak je dostupna iz menia za upravljanje dodacima
* Prečica za dobijanje dropbox statusa je promenjena u NVDA+alt+d kako bi se
  izbegli konflikti sa prečicom za stišavanjem pozadinskih zvukova 

## promene u 3.1 ##

* Koristi se drugi način da se dođe do dugmeta otkaži i kartica. Sada ne
  moramo doći do njih pre korišćenja prečica.
* Kada se promeni aktivna kartica, fokus će biti premešten na nju pa kada
  pritisnete tab, Prva stavka će biti prikazana umesto da fokus ostane na
  prethodnoj kartici iako više nije aktivna.
* U dijalogu za podešavanja, možete menjati kartice sa prečicama
  control+page up-down. Control+tab i shift+tab idalje rade.
* Sve lokalizovane manifest datoteke sada treba da budu uredu.
* Manje ispravke

## promene u 3.0 ##

* Male ispravke u glavnoj manifest datoteci (autori su ispravno prikazani).
* Poboljšana detekcija kontekstnog menija kada pritisnete NVDA+alt+d 3 puta
* Escape taster sada radi(samo kada koristite NVDA i dropbox na istom
  jeziku)
* Dosta ispravki u kodu
* dodata-ažurirana dokumentacija svih skripti
* Novi jezici : Arapski, Brazilsko portugalski, Češki, Belgijski, Finski,
  Galski, Nemački, Mađarski, Japanski, Nepali, Poljski, Ruski, Španski,
  Slovački, Tamil, Turski.

## Promene u 2.0 ##

* Novi jezici: Italijanski
* Ako se pritisne NVDA+alt+d 3 puta kada ste već u kontekstnom meniju, više
  ne dolazi do problema

## Promene u 1.0 ##

* Prva verzija

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
