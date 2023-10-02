# dropbox #

* Fejlesztők: Patrick ZAJDA, Filaos és egyéb közreműködők
* NVDA compatibility: NVDA 2019.1 or later
* Letöltés [stabil verzió][1]
* Download [development version][2]

This plugin add a shortcut to announce Dropbox status or open the Dropbox
systray menu when pressed once or twice respectively.  It also enhances
DropBox item lists.

* Parancsbillentyű: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the
  announcement of the version

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
