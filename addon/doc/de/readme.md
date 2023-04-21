# dropbox #

* Autoren: Patrick ZAJDA <patrick@zajda.fr>, Filaos und andere Entwickler
* NVDA-Kompatibilität: 2019.1 oder neuer
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung fügt eine Tastenkombination hinzu, um den Dropbox-Status
anzusagen oder das Dropbox-Menü zu öffnen, wenn Sie ein- bzw. zweimal
gedrückt wird.  Außerdem werden DropBox-Elementlisten verbessert.

* Tastenkürzel: NVDA+Alt+D


## Änderungen in 4.6 ##

* NVDA-Kompatibilität: 2021.1

## Änderungen in 4.4 ##

* Kompatibilität zu Python 3
* Verwendung der letzten Erweiterungsvorlage
* Änderung am Repository vorgenommen, damit die Erweiterung mit Appveyor
  erstellt wird
* Falsche Tastenkürzel korrigiert und nicht verwendete Tastenkombinationen
  aus der Dokumentation entfernt
* Die Beschreibung wurde in der Dokumentation aktualisiert, da diese noch
  die Ankündigung der Version enthielt

## Änderungen in 4.0 ##

* Die Hilfe zur Erweiterung ist im Dialogfeld \"Erweiterungen verwalten\"
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
* Kleinere Korekturen.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
