# Dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* Download [stabiele versie][1]
* Download [development version][2]

Deze add-on voegt een sneltoets toe om de status, versie en het contextmenu
van Dropbox op te vragen. Verder werkt het wisselen van tabbladen in de
instellingen met ctrl+tab en kan de Annuleren knop met escape worden
geactiveerd.

* Shortcut: NVDA+Alt+D
* Ctrl+Alt+T meldt het actieve tabblad.

## Bekende problemen ##

* Als u van tabbladen wisselt met de sneltoetsen en het venster sluit, zal NVDA niet weten dat het venster gesloten is.
Dit is een bekend probleem in NVDA en kan niet worden opgelost.


## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor

## Veranderingen voor 4.0 ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## Veranderingen voor 3.1 ##

* Een andere manier om de Annuleren knop te vinden, nu hoeft deze niet eerst
  de focus te krijgen
* Als het actieve tabblad gewijzigd wordt, verplaatst de focus naar het
  nieuwe tabblad en blijft niet langer hangen op het vorige tabblad
* In het voorkeurenvenster kan nu ook met ctrl+pageup/pagedown van tabblad
  worden gewisseld. Ctrl+tab en ctrl+shift+tab kunnen ook nog steeds
  gebruikt worden.
* Alle vertaalde manifest-bestanden kloppen nu.
* Kleine verbeteringen.

## Veranderingen voor 3.0 ##

* Kleine verandering in het manifest-bestand waardoor de auteurs goed worden
  weergegeven.
* Detectie van het contextmenu is verbeterd bij drie maal drukken van
  NVDA+shift+d.
* De escape-toets voor het sluiten van de instellingen werkt enkel als
  Dropbox dezelfde taal gebruikt als NVDA.
* Veel fouten opgelost.
* Documentatie voor alle scripts toegevoegd/bijgewerkt.
* Nieuwe vertalingen: Arabisch, Braziliaans Portugees, Tsjechisch,
  Nederlands, Fins, Gallisch, Duits, Hongaars, Japans, Nepalees, Pools,
  Russisch, Spaans, Slovaaks, Tamil, Turks.

## Veranderingen voor 2.0 ##

* Nieuwe vertalingen: Italiaans
* Drie maal of vaker de sneltoets indrukken terwijl het contextmenu al open
  is, geeft geen problemen meer.

## Veranderingen voor 1.0 ##

* Eerste versie

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx

[2]: https://addons.nvda-project.org/files/get.php?file=dx-dev
