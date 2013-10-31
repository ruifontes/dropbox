# dropbox #

* Autorzy: Patrick ZAJDA <patrick@zajda.fr>, Filaos i inni.
* Download [stable version][1]
* Download [development version][2]

WTyczka dodaje do NVDA skrót klawiszowy, po którego wciśnięciu otrzymujemy
informację o statusie programu, jego wersji, a także ułatwia pracę z menu
kontekstowym tego programu oraz jego oknem preferencji.

* skrót: nvda+shift+d
* control+alt+t zgłasza aktywną zakładkę ustawień dropbox

## znane błędy ##

*Jeśli użyjesz skrutu klawiszowego do przechodzenia między zakładkami i zamkniesz okno ustawień wtyczki, NVDA może nie odnotować zniknięcia tego okna.
Jest to znany problem z NVDA, który nie może być poprawiony.

## Changes for 4.0 ##

* Translations update.
* Fixed issues with windows 8 metro app.

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

[1]: http://addons.nvda-project.org/files/get.php?file=dx

[2]: http://addons.nvda-project.org/files/get.php?file=dx-dev
