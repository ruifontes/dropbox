# dropbox #

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos a ďalší
* NVDA compatibility: NVDA 2019.1 or later
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]

Na prvé stlačenie klávesovej skratky Oznamuje stav Dropboxu. Dvojité
stlačenie klávesovej skratky otvorí kontextové menu. Tiež upravuje
prístupnosť položiek v menu.

* Skratka: NVDA+alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Zmeny vo verzii 4.4 ##

* Kompatibilné s prostredím Python 3
* Používa šablónu posledného doplnku
* Repozitár je postavený na Appveyor
* Odstránené nepoužívané klávesové skratky z dokumentácie
* Upravený popis v návode k doplnku a odstránená informácia o oznamovaní
  verzie

## Zmeny vo verzii 4.0 ##

* Pomocník k doplnku je dostupný zo správcu doplnkov.
* Klávesová skratka zmenená na nvda+alt+d, aby nedochádzalo ku konfliktom s
  funkciou stíšenia.

## Zmeny vo verzii 3.1 ##

* Používa sa lepší spôsob na získanie cesty k tlačidlu zrušiť (cancel). Nie
  je viac potrebné naň prejsť. Takisto záložky nemusia viac získať fokus
  pred použitím skratiek.
* pri zmene aktívnej záložky sa tiež zmení fokus tak, že je na prvej položke
  novej záložky a nie na položke starej záložky, ktorá viac nie je aktívna.
* na prechod medzi záložkami sa dajú použiť skratky  ctrl+page
  up/down. Ctrl+tab a ctrl+shift+tab ostali zachované.
* Všetky manifest súbory by mali byť v poriadku.
* Drobné úpravy.

## Zmeny vo verzii 3.0 ##

* Úprava v súbore manifest (autori sa zobrazujú správne)
* Zlepšená podpora pre zobrazenie kontextovej ponuky po trojitom stlačení
  nvda+shift+D.
* Ak používate NVDA v tom istom jazyku, ako Dropbox, funguje kláves Escape.
* Mnoho úprav v kóde.
* Pridaná a aktualizovaná dokumentácia pre skratky.
* Nové jazyky: Arabčina, Brazílska portugalčina, Čeština, Holandčina,
  Fínčina, Galijcíčina, Nemčina, Maďarčina, japončina, Nepálčina, Poľština,
  Ruština, Španielčina, Slovenčina, Tamilčina, Turečtina.

## Zmeny vo verzii 2.0 ##

* Preložený do Taliančiny
* Stlačenie NVDA+Shift+D trikrát alebo viac, ak je fokus už v kontextovom
  menu nespôsobuje problémy.

## Zmeny vo verzii 1.0 ##

* Prvé vydanie

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
