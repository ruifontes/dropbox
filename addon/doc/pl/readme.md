# dropbox #

* Autorzy: Patrick ZAJDA <patrick@zajda.fr>, Filaos i inni współautorzy
* NVDA compatibility: NVDA 2019.1 or later
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

This plugin add a shortcut to announce Dropbox status or open the Dropbox
systray menu when pressed once or twice respectively.  It also enhances
DropBox item lists.

* skrót: nvda+alt+d


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Zmiany dla wersji 4.4 ##

* Zgodność z Pythonem 3
* Używanie ostatniego szablonu dodatków
* Zmiany repozytorium dla możliwości budowy z Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the
  announcement of the version

## zmiany dla 4.0 ##

* Pomoc dodatku jest dostępna z menedżera dodatków.
* Skrót do pobierania statusu Dropbox został zmieniony na Alt+NVDA+D aby
  zapobiec konflikt z wsparciem do przyciszania głośności.

## zmiany dla wersji 3.1 ##

* Używa innej metody do znalezienia przycisku Anuluj i zakładki
  strony. Teraz nie musimy jej lokalizować punktem uwagi przed użyciem
  skrótu.
* Gdy zmienisz aktywną zakładkę, punkt uwagi przemieszcza się na kartę z
  zakładkami. Zatem gdy wciśniesz tab, aktywowany zostanie pierwszy element
  zakładki
* w oknie ustawień można poruszać się między zakładkami używając kombinacji
  ctrl+page up i page down
* tłumaczone pliki.manifest nie powinny sprawiać problemów.
* drobne poprawki.

## zmiany dla 3.0 ##

* poprawki pliku manifest (autorzy są pokazywani prawidłowo)
* poprawione wykrywanie menu kontekstowego po trzykrotnym wciśnięciu
  nvda+shift+d
* Klawisz escape działa tylko, gdy język dropboxa jest taki sam, jak język
  NVDA
* wiele poprawek w kodzie skryptu
* dodano zaktualizowaną dokumentację
* Komunikaty w nowych językach: Arabski, Brazylijski portugalski,, Czeski,
  Duński, Fiński, Galicyjski, Niemiecki, Wengierski, Japoński, Nepalski,
  Polski, Rosyjski, Chiszpański, Słowacki, Tamil, Turecki.

## zmiany dla wersji 2.0 ##

* nowy język: Włoski
* trzykrotne wciśnięcie skrótu, gdy jest się już w menu kontekstowym, nie
  sprawia problemów

## zmiany dla wersji 1.0 ##

* wstępne wydanie

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx

[2]: https://addons.nvda-project.org/files/get.php?file=dx-dev
