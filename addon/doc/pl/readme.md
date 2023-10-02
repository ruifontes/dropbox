# dropbox #

* Autorzy: Patrick ZAJDA <patrick@zajda.fr>, Filaos i inni współautorzy
* Zgodność z NVDA: NVDA 2019.1 lub nowsza
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ta wtyczka dodaje skrót do ogłaszania statusu Dropbox lub otwierania menu
systray Dropbox po naciśnięciu odpowiednio raz lub dwa razy.  Ulepsza
również listy elementów DropBox.

* Skrót: NVDA+Alt+D


## Zmiany w wersji 4.6 ##

* Określanie zgodności z NVDA 2021.1

## Zmiany dla wersji 4.4 ##

* Zgodność z Pythonem 3
* Używanie ostatniego szablonu dodatków
* Zmiany repozytorium dla możliwości budowy z Appveyor
* Naprawiono błędy i usunięto nieużywane skróty w dokumentacji
* Zaktualizuj opis w dokumentacji, która nadal odnosiła się do ogłoszenia
  wersji

## Zmiany w wersji 4.0 ##

* Pomoc dodatku jest dostępna z menedżera dodatków.
* Skrót do pobierania statusu Dropbox został zmieniony na Alt+NVDA+D aby
  zapobiec konflikt z wsparciem do przyciszania głośności.

## Zmiany w wersji 3.1 ##

* Używa innej metody do znalezienia przycisku Anuluj i zakładki
  strony. Teraz nie musimy jej lokalizować punktem uwagi przed użyciem
  skrótu.
* Podczas zmiany aktywnej karty fokus przenosi się na stronę karty, więc po
  naciśnięciu Tab pierwszy element karty jest aktywowany zamiast pozostawać
  na poprzedniej używanej karcie, nawet jeśli nie jest już aktywowany.
* W oknie dialogowym preferencji można teraz nacisnąć control+page w górę/w
  dół, aby przełączać się między kartami. Control+tab i control+shift+tab
  nadal działają.
* Wszystkie zlokalizowane pliki manifestów powinny być teraz w porządku.
* Drobne poprawki.

## Zmiany w wersji 3.0 ##

* Drobna korekta w głównym pliku manifestu (autorzy są poprawnie
  wyświetleni).
* Ulepszono wykrywanie menu kontekstowego po trzykrotnym naciśnięciu
  Shift+NVDA+D.
* Przycisk Escape działa teraz (tylko w przypadku korzystania z Dropbox w
  tym samym języku, którego używa NVDA).
* Dużo poprawek w kodzie.
* Dodano/zaktualizowano dokumentację wszystkich skryptów.
* Komunikaty w nowych językach: Arabski, Brazylijski portugalski,, Czeski,
  Duński, Fiński, Galicyjski, Niemiecki, Wengierski, Japoński, Nepalski,
  Polski, Rosyjski, Chiszpański, Słowacki, Tamil, Turecki.

## Zmiany w wersji 2.0 ##

* Nowe języki: włoski
* Naciśnięcie skrótu trzy razy lub więcej, gdy jest już w menu kontekstowym,
  nie powoduje już problemu.

## Zmiany w wersji 1.0 ##

* Wstępne wydanie

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
