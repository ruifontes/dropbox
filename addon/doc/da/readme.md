# Dropbox #

* Forfattere: Patrick ZAJDA, Filaos og andre bidragydere
* NVDA -kompatibilitet: NVDA 2019.1 eller nyere
* Download [stabil version][1]
* Download [udviklingsversion][2]

Dette tilføjelsesprogram tilføjer en genvejstast, som annoncerer status for
Dropbox eller åbne Dropbox-menuen i systembakken ved at udføre kommandoen to
gange lige efter hinanden. Desuden virker skift af faneblade i
Indstillinger-dialogen med Ctrl+Tab og Shift+Ctrl+Tab samt med
Ctrl+side-op/ned. Afslutningsvis virker Annuller-knappen med Escape.

* Genvejstast: NVDA+Alt+D


## Ændringer for 4.6 ##

* Angiv kompatibilitet med NVDA 2021.1

## Ændringer i 4.4 ##

* Python 3-kompatibilitet
* Brug den sidste tilføjelsesskabelon
* Lagringsændring, der skal bygges med Appveyor
* Rettet forkert og fjernet ubrugte genveje i dokumentationen
* Opdaterede beskrivelsen i dokumentationen, som stadig henviste til
  annonceringen af versionen

## Ændringer i4.0  ##

* Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
  tilføjelsesprogrammer.
* Genvejen til at få fat i status for Dropbox er blevet ændret til
  Alt-NVDA-d for at undgå konflikt med understøttelse af audio ducking.

## Ændringer i 3.1 ##

* Bruger en anden måde til at få fat i Annuller-knappen og faneblade. Det er
  nu ikke nødvendigt at bringe dem i fokus, før man bruger genvejstasterne.
* Når man skifter det aktive faneblad, flytter fokus nu til fanebladet, så
  når man trykker Tab, kommer man til det første felt på det aktive faneblad
  i stedet for at blive på det forrige faneblad, selv om det ikke længere er
  aktivt.
* I Indstillinger-dialogen er det nu muligt at trykke Ctrl+Side-op/ned for
  at skifte mellem faneblade. Ctrl+Tab og Ctrl+Shift+Tab virker stadig.
* Alle lokaliserede manifest-filer skulle nu være OK.
* Mindre rettelser.

## Ændringer i 3.0 ##

* Mindre rettelse i hovedmanifestfilen. Forfattere bliver nu vist rigtigt.
* Forbedret detektering af kontekstmenuen ved tre tryk på NVDA+Shift+d.
* Escape-tasten virker nu (kun hvis man bruger Dropbox på det samme sprog
  som NVDA.
* Mange rettelser til koden.
* Tilføjet/opdateret dokumentation af alle scripts.
* Nye sprog: Arabisk, brasiliansk/portugisisk, tjekkisk, hollandsk, finsk,
  galicisk, tysk, ungarsk, japansk, nepalesisk, polsk, russisk, spansk
  slovakisk, tamil, tyrkisk, 

## Ændringer i 2.0 ##

* Nye sprog: Italiensk.
* Det giver ikke længere problemer, hvis man trykker tre gange eller mere på
  genvejstasten, mens man allerede står i kontekstmenuen.

## Ændringer i 1.0 ##

* Første udgivelse

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
