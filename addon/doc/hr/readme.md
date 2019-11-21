# dropbox #

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos i drugi suradnici
* Preuzmi [stabilnu verziju][1]

Ovaj će dodatak dodati prečac koji izgovara stanje Dropboxa, verziju ili
otvara Dropboxov izbornik u platformi sustava. Omogućuje premještanje po
karticama dijaloškog okvira postavki, pomoću Ctrl+tab/Ctrl+shift+tab i/ili
Ctrl+Stranica gore/Ctrl+Stranica dolje. Ukratko, ovaj dodatak omogućuje
upotrebu gumba „Odustani” pomoću tipke escape.

* Prečac: NVDA+Shift+D
* Ctrl+Alt+T Izgovori aktivnu karticu svojstva.

## Poznati problemi ##

* Prilikom prebacivanja između kartica uz pomoć prečaca, kad se zatvori prozor s postavkama, NVDA dobiva krivu informaciju o otvorenim prozorima.
Radi se o poznatom NVDA problemu, koji nije moguće ispraviti.


## Izmjene u verziji 4.0 ##

* Pomoć za ovaj dodatak je dostupna u Upravljaču dodataka.
* Prečac za dobivanje Dropbox stanja je promijenjen u Alt+NVDA+D, kako bi se
  izbjegli konflikti s podrškom za stišavanje zvukova.

## Izmjene u verziji 3.1 ##

* Koristi neki drugi način za gumb „Odustani” i prebacivanje između
  kartica. Sada ih više nije potrebno fokusirati prije korištenja prečaca.
* Kad se mijenja aktivna kartica, fokus se premješta na karticu stranice,
  tako da se pritiskom tabulatora aktivira prva stavka na kartici, umjesto
  da ostane na prethodno korištenoj kartici, čak iako više nije aktivirana.
* U dijaloškom okviru postavki je sada moguće pritisnuti control+stranica
  gore/dolje, za prebacivanje između kartica. Tipke control+tab i
  control+shift+tab rade i dalje.
* Sve lokalizirane manifest datoteke bi sad trebale biti u redu.
* Manji ispravci.

## Promjene u verziji 3.0 ##

* Manji ispravci u glavnoj manifest datoteci (autori se ispravno prikazuju).
* Poboljšano otkrivanje kontekstnog izbornika, kad se Shift+NVDA+D pritisne
  tri puta.
* Tipka escape sada radi (samo kad Dropbox koristi isti jezik, koji koristi
  i NVDA).
* Mnogi ispravci u kodu.
* Dodana/aktualizirana dokumentacija svih skripti.
* Novi jezici: Arapski, Brazilski portugalski, Češki, Nizozemski, Finski,
  Galicijski, Njemački, Mađarski, Japanski, Nepalski, Poljski, Ruski,
  Španjolski, Slovački, Tamilski, Turski.

## Promjene u verziji 2.0 ##

* Novi jezik: Talijanski
* Kad se prečac u kontekstnom izborniku pritisne tri puta ili više, ne
  dolazi do problema.

## Promjene u verziji 1.0 ##

* Prva verzija

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
