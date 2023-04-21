# dropbox #

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos e altri collaboratori
* NVDA compatibility: NVDA 2019.1 or later
* Scarica [versione stabile][1]
* Scarica [versione in sviluppo][2]

Questo addon aggiunge un tasto rapido per vocalizzare lo stato di Dropbox,
oppure aprire il menu di Dropbox nel System Tray, quando viene premuto una o
due volte rispettivamente. Inoltre migliora la gestione degli elenchi in
Dropbox.

* Tasto rapido: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Novità nella versione 4.4 ##

* Compatibilità con Python 3
* Utilizza l'ultimo template per gli addon
* MOdifiche al repository, perché possa essere realizzato con Appveyor
* Nella documentazione, corretti i tasti rapidi errati e rimossi quelli non
  usati
* Nella documentazione, aggiornata la descrizione, che faceva ancora
  riferimento alla vocalizzazione della versione

## Novità nella versione 4.0 ##

* La guida è disponibile dal gestore componenti aggiuntivi.
* Il tasto di scelta rapida per ottenere lo stato di Dropbox è stato
  modificato in alt+NVDA+d per evitare conflitti con il supporto
  all'attenuazione audio.

## Novità nella versione 3.1 ##

* Viene utilizzato un nuovo metodo per intercettare il pulsante annulla e le
  schede. Ora non c'è bisogno di focalizzare tali elementi per usare i tasti
  rapidi.
* Quando viene modificata la scheda attiva, il focus viene spostato su di
  essa, di modo che, quando viene premuto il tasto tab, si passi subito al
  primo elemento della scheda scelta.
* Nella finestra di dialogo Preferenze, è ora possibile premere control +
  pagina su / giù per passare da una scheda all'altra. Ctrl + Tab e Ctrl +
  Maiusc +tab continuano a funzionare.
* Tutti i file manifest tradotti dovrebbero essere ora corretti.
* Correzioni minori.

## Novità nella versione 3.0 ##

* Correzioni varie nel file manifest.ini nel nome degli autori.
* Migliorato il rilevamento del menu di contesto quando viene premuto
  NVDA+Shift+d tre volte.
* Ora il tasto Escape funziona soltanto se Dropbox e NVDA sono configurati
  per usare la stessa lingua.
* Diverse correzioni nel codice.
* Aggiunta/aggiornata la documentazione di tutti gli script.
* Nuove lingue: Arabo, Portoghese Brasiliano, Ceco, Olandese, Finlandese,
  Galiziano, Tedesco, Ungherese, Giapponese, Nepalese, Polacco, Russo,
  Spagnolo, Slovacco, Tamil, Turco.

## Novità nella versione 2.0 ##

* Nuove Lingue: Italiano
* La pressione del tasto rapido per tre volte o più, quando ci si trova nel
  menu di contesto, non causa più alcun problema.

## Novità nella versione 1.0 ##

* Prima versione

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
