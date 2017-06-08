# dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* Stiahnuť [stabilná verzia][1]

Oznamuje stav Dropboxu, jeho verziu a umožňuje otvoriť kontextové menu
programu z klávesnice. Môžete sa tiež pohybovať po záložkách v možnostiach
programu pomocou ctrl+tab a  Shift+Ctrl+Tab resp ctrl+page up /down. Okno s
nastaveniami sa dá zatvoriť tlačidlom Escape.

* Shortcut: NVDA+Alt+D
* Ctrl+Alt+T oznámi názov aktívnej záložky.

## Známe problémy ##

* Ak sa presúvate medzi záložkami pomocou klávesových skratiek a zatvoríte okno s bnastaveniami Dropboxu, NVDA si nevšimne, že okno je zatvorené.
Toto je známa chyba a nedá sa odstrániť.


## Zmeny vo verzii 4.0 ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## Zmeny vo verzii 3.1 ##

* Používa sa lepší spôsob na získanie cesty k tlačidlu zrušiť (cancel). Nie
  je viac potrebné naň prejsť a záložká. Nemusia viac získať fokus pred
  použitím skratky.
* pri zmene aktívnej záložky sa tiež zmení fokus tak, že je na prvej položke
  novej záložky a nie na položke starej záložky, ktorá viac nie je aktívna.
* na prechod medzi záložkami sa dajú použiť skratky  control+page
  up/down. Control+tab a control+shift+tab ostali zachované.
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

[1]: https://addons.nvda-project.org/files/get.php?file=dx
