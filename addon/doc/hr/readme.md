# dropbox #

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos i drugi suradnici
* NVDA kompatibilnost: NVDA 2019.1 ili novija
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj će dodatak dodati prečac koji javlja stanje Dropboxa, verziju ili
otvara Dropboxov izbornik u platformi sustava. Omogućuje premještanje po
karticama dijaloškog okvira postavki, pomoću Ctrl+tab/Ctrl+shift+tab i/ili
Ctrl+Stranica gore/Ctrl+Stranica dolje. I na kraju, ovaj dodatak omogućuje
upotrebu gumba „Odustani” pomoću tipke escape.

Ovaj dodatak dodaje prečac za objavljivanje Dropbox stanja ili za otvaranje
Dropbox izbornik u programskoj traci, kad se pritisne jedanput, odnosno
dvaput. Također poboljšava popise elemenata DropBoxa.

* Prečac: NVDA+šift+D


## Izmjene u verziji 4.6 ##

* Specificiraj NVDA 2021.1 kompatibilnost

## Izmjene u verziji 4.4 ##

* Python 3 kompatibilnost
* Koristi zadnji predložak dodatka
* Promjena u repozitoriju kako bi se izgradio s Appveyor
* U dokumentaciji su popravljeni pogrešni te uklonjeni neiskorišteni prečaci
* Aktualiziran je opis u dokumentaciji, koji još uvijek upućuje na najavu
  verzije

## Izmjene u verziji 4.0 ##

* Pomoć za ovaj dodatak je dostupna u stavci Upravljanje dodacima.
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
* Sve lokalizirane manifest datoteke bi sada trebale biti u redu.
* Manji ispravci.

## Promjene u verziji 3.0 ##

* Manji ispravci u glavnoj manifest datoteci (autori se ispravno prikazuju).
* Poboljšano otkrivanje kontekstnog izbornika, kad se šift+NVDA+D pritisne
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
