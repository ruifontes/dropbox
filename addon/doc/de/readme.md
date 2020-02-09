# dropbox #

* Autoren: Patrick ZAJDA <patrick@zajda.fr>, Filaos und andere Entwickler
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung fügt ein Tastenkürzel hinzu, dass den Status von Dropbox,
die Version ansagt oder  das Dropbox-Kontextmenü öffnet. Des weiteren kann
man in den Optionen mittels STRG+Tab und STRG+Umschalt+Tab sowie STRG+Seite
auf bzw. STRG+Seite ab navigieren. Außerdem funktioniert nun der
abbrechen-Schalter

* Tastenkürzel: NVDA+Alt+D
* STRG+Alt+T aktive Registerkarte ansagen.

## bekannte Fehler ##

* Wenn Sie nach dem Schließen des Einstellungsfensters die Tastenkombination zum Wechseln der Registerkarten verwenden, wird NVDA so reagieren, als ob das Fenster immernoch offen ist.
Dieses Problem kann zur Zeit nicht behoben werden.


## Änderungen in 4.4 ##

* Kompatibilität zu Python 3
* Es wird die letzte Vorlage für Erweiterungen verwendet.
* Änderung am Repository vorgenommen, damit die Erweiterung mit Appveyor
  erstellt wird.

## Änderungen in 4.0 ##

* die Hilfe zur Erweiterung ist im Dialogfeld \"Erweiterungen verwalten\"
  abrufbar.
* Die Tastenkombination zum Umgang mit der Erweiterung wurde auf alt+nvda+d
  geändert, um Konflikte mit der Funktion zum Verringern der lautstärke
  anderer Audioquellen unter Windows 8.1 und neuer zu verhindern.

## Änderungen in 3.1 ##

* Der Schalter "abbrechen" und die Registerkarten werden nun anders
  ermittelt. beides muss nicht mehr fokussiert werden, wenn Tastenkürzel
  verwendet werden sollen.
* Wenn Sie zwischen den Registerkarten wechseln, wird nun immer der erste
  Eintrag der neuen Registerkarte hervorgehoben.
* In den Einstellungen können Sie nun mittels Steuerung+seite auf bzw. Seite
  ab zwischen den Registerkarten wechseln. STRG+Tab bzw. Umschalt+Tab
  funktioniert weiterhin.
* Alle übersetzten Manifest-Dateien sollten nun in Ordnung sein.
* kleinere Korekturen

## Änderungen in 3.0 ##

* Kleinere Korrektur in der manifest-Datei (authoren werden richtig
  dargestellt).
* Verbesserte Erkennung des Kontextmenüs, wenn NVDA+Umschalt+D 3mal gedrückt
  wird.
* Die Escape-Taste zum Abbrechen  funktioniert nun nur noch, wenn Dropbox
  die gleiche Sprache wie NVDA nutzt.
* Viele Korekturen im Quellcode.
* Dokumentation für alle Skripte wurde hinzugefügt bzw. aktualisiert.
* Neue Sprachen: arabisch, Brasilianisches portugisisch, tschechisch,
  niderländisch, finnisch, gälisch, deutsch, ungarisch, japanisch,
  nepalesisch, polisch, russisch, spanisch, slowakisch, tamil, türkisch.

## Änderungen in 2.0 ##

* Neue Sprachen: Italienisch
* Wenn Sie das Tastenkürzel 3- oder mehr mals betätigen, wenn Sie sich im
  Dropbox-Menü befinden, treten keine Probleme mehr auf.

## Änderungen in 1.0 ##

* Erstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx

[2]: https://addons.nvda-project.org/files/get.php?file=dx-dev
