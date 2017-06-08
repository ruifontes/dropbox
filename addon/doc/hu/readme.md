# dropbox #

* Fejlesztők: Patrick ZAJDA, Filaos és egyéb közreműködők
* Letöltés [stabil verzió][1]

A kiegészítő segítségével lekérdezhető a Dropbox program állapota, verziója,
valamint megnyitható a menüje egy billentyűparancs segítségével. A
beállítások párbeszédablak lapfülei helyesen hangoznak el a ctrl+tab és
ctrl+shift+tab, vagy a ctrl+page up/down használatakor. Az Escape
billentyűvel az ablak bezárható.

* Parancsbillentyű: NVDA+Alt+D
* Ctrl+Alt+T bemondja az aktív lapfület.

## Ismert hibák ##

* Ha a billentyűparancsok használatával vált a lapfülek között, az NVDA nem észleli a tulajdonságok ablak bezárását.
Ez egy ismert hiba, amit nem lehet javítani.


## A 4.0 verzió változásai ##

* A bővítmény súgója elérhető a bővítménykezelőben.
* A dropbox állapotának lekérdezésére szolgáló gyorsgomb Alt+NVDA+D lett,
  hogy ne ütközzön a hangerő-igazítás beállításával.

## A 3.1 verzió változásai ##

* Más módszer a lapfül és a mégse gomb megállapításához. Most már nem kell a
  fókuszt rájuk helyezni billentyűparancsok használatakor.
* Ha az aktív fület megváltoztatja, a fókusz a tulajdonságlapra lép, így a
  tab megnyomása esetén az első elem lesz aktív a fülön, nem pedig a
  legutoljára használt fül. Ez akkor is működik, ha a lapfül vezérlő nincs a
  fókuszban.
* A beállítások párbeszédablakon már a ctrl+page up/down billentyűparanccsal
  is lehetőség van a lapfülek közötti navigációra. A ctrl+tab és
  ctrl+shift+tab úgyszintén működik.
* Az összes lefordított manifest fájl működik.
* Kisebb javítások

## A 3.0 verzió változásai ##

* Kisebb javítások az eredeti manifest fájlban (a készítők nevei helyesen
  jelennek meg)
* A helyi menü elérésének fejlesztése, amikor a Shift+NVDA+D
  billentyűparancsot háromszor lenyomják.
* Az escape gomb csak akkor működik, ha a Dropbox azt a nyelvet használja
  mint az NVDA
* Rengeteg javítás a kódban
* A szkriptek dokumentációjának hozzáadása/frissítése
* Új nyelvek: Arab, Brazil portugál, Cseh, Holland, Finn, Galiciai, Német,
  Magyar, Japán, Nepáli, Lengyel, Orosz, Spanyol, Szlovák, Tamil, Török.

## A 2.0 verzió változásai ##

* Új nyelv: Olasz
* A parancsbillentyű háromszori megnyomása a menüben már nem okoz problémát.

## Az 1.0 verzió változásai ##

* Az első kiadás

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
