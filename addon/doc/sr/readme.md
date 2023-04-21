# dropbox #

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos i drugi saradnici
* NVDA kompatibilnost: NVDA 2019.1 ili noviji
* Preuzmi [stabilnu verziju][1]
* Preuzmi [verziju u razvoju ][2]

Ovaj dodatak dodaje prečicu za izgovor dropbox statusa ili otvaranje menija
u sistemskoj traci.  Takođe poboljšava stavke u Dropbox listama.

* Prečica: NVDA+alt+d


## Promene u 4.6 ##

* Naznačena NVDA 2021.1 kompatibilnost

## Promene u 4.4 ##

* Python 3 kompatibilnost
* Koristi se najnoviji template za dodatke
* Promena u repository kako bi se koristio Appveyor
* Ispravljene netačne i uklonjene prečice koje se ne koriste iz
  dokumentacije
* Ažuriran opis u dokumentaciji koja je napominjala izgovor verzije

## Promene u 4.0 ##

* Pomoć za dodatak je dostupna iz menia za upravljanje dodacima.
* Prečica za dobijanje dropbox statusa je promenjena u NVDA+alt+d kako bi se
  izbegli konflikti sa prečicom za stišavanje pozadinskih zvukova.

## promene u 3.1 ##

* Koristi se drugi način da se dođe do dugmeta otkaži i kartica. Sada ne
  moramo doći do njih pre korišćenja prečica.
* Kada se promeni aktivna kartica, fokus će biti premešten na nju pa kada
  pritisnete tab, Prva stavka će biti prikazana umesto da fokus ostane na
  prethodnoj kartici iako više nije aktivna.
* U dijalogu za podešavanja, možete menjati kartice sa prečicama
  control+page up-down. Control+tab i shift+tab i dalje rade.
* Sve lokalizovane manifest datoteke sada treba da budu u redu.
* Manje ispravke.

## promene u 3.0 ##

* Male ispravke u glavnoj manifest datoteci (autori su ispravno prikazani).
* Poboljšana detekcija kontekstnog menija kada pritisnete NVDA+alt+d 3 puta.
* Escape taster sada radi(samo kada koristite NVDA i dropbox na istom
  jeziku).
* Dosta ispravki u kodu.
* dodata-ažurirana dokumentacija svih skripti.
* Novi jezici : Arapski, Brazilsko portugalski, Češki, Belgijski, Finski,
  Galski, Nemački, Mađarski, Japanski, Nepali, Poljski, Ruski, Španski,
  Slovački, Tamil, Turski.

## Promene u 2.0 ##

* Novi jezici: Italijanski
* Ako se pritisne NVDA+alt+d 3 puta kada ste već u kontekstnom meniju, više
  ne dolazi do problema.

## Promene u 1.0 ##

* Prva verzija

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
