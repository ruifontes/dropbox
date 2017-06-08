# dropbox #

* Autoren: Patrick ZAJDA <patrick@zajda.fr>, Filaos und andere Entwickler
* [Stabile Version herunterladen][1]

Diese Erweiterung fügt ein Tastenkürzel hinzu, dass den Status von Dropbox,
die Version ansagt oder  das Dropbox-Kontextmenü öffnet. Des weiteren kann
man in den Optionen mittels Steuerung+Tabulator und
Steuerung+Umschalt+Tabulator sowie Steuerung+Seite rauf bzw. Steuerung+Seite
runternavigieren. Des weiteren funktioniert nun der abbrechen-Schalter

* Tastenkürzel: NVDA+Alt+D
* STRG+Alt+T aktive Registerkarte ansagen.

## bekannte Fehler ##

* Wenn Sie die Tastenkombination zum Wechseln der Registerkarten verwenden, nachdem Sie das Einstellungsfenster geschlossen haben, wird NVDA nicht gewahr, dass das Fenster nicht mehr existiert.
Dieses Problem kann zur Zeit nicht behoben werden.


## Änderungen bis 4.0 ##

* die Hilfe zur Erweiterung ist im Dialogfeld \"Erweiterungen verwalten\"
  abrufbar.
* Die Tastenkombination zum Umgang mit der Erweiterung wurde auf alt+nvda+d
  geändert, um Konflikte mit der Funktion zum Verringern der lautstärke
  anderer Audioquellen unter Windows 8.1 und neuer zu verhindern.

## Änderungen bis 3.1 ##

* Der Schalter "abbrechen" und die Karteireiter werden nun anders ermittelt,
  beides muss nicht mehr fokussiert werden.
* Wenn Sie zwischen den Registerkarten wechseln, wird nun immer der erste
  Eintrag der neuen Registerkarte hervorgehoben.
* In den Einstellungen können Sie nun mittels Steuerung+seite rauf
  bzw. runter zwischen den Registerkarten wechseln. Steuerung+Tabulator
  bzw. Umschalt+Tabulator funktioniert weiterhin.
* Alle übersetzten Manifest-Dateien sollten nun in Ordnung sein.
* kleinere Korekturen

## Änderungen bis 3.0 ##

* Kleinere Korrektur in der manifest-Datei (authoren werden richtig
  dargestellt).
* Verbesserte Erkennung des Kontextmenüs, wenn NVDA+Umschalt+D 3mal gedrückt
  wird.
* Der Schalter "abbrechen" funktioniert nun nur noch, wenn Dropbox die
  gleiche Sprache wie NVDA nutzt.
* Viele Korekturen im Quellcode.
* Dokumentation für alle Skripte hinzugefügt bzw. aktualisiert.
* Neue Sprachen: arabisch, Brasilianisches portugisisch, tschechisch,
  niderländisch, finnisch, gälisch, deutsch, ungarisch, japanisch,
  nepalesisch, polisch, russisch, spanisch, slowakisch, tamil, türkisch.

## Änderungen bis 2.0 ##

* Neue Sprachen: Italienisch
* Wenn Sie das Tastenkürzel 3- oder mehr mals betätigen, wenn Sie sich im
  Dropbox-Menü befinden, treten keine Probleme mehr auf.

## Änderungen bis 1.0 ##

* Erstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
