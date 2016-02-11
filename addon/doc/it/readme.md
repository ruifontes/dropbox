# dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* Download [stable version][1]

Questo componente aggiuntivo aggiungerà un tasto di scelta rapida per
annunciare lo stato di Dropbox, il numero di versione oppure aprire il menu
di Dropbox nel System Tray. Inoltre, possono essere usati i tasti
control+tab control+shift+tab e control+paginaSu/giùper muoversi tra le
schede nelle preferenze di Dropbox.   Per concludere, il tasto annulla
funzionerà anche premendo Esc.

* Shortcut: NVDA+Alt+D
* Ctrl+Alt+T annuncia la scheda attiva.

## Problemi noti ##

* Se si passa da una scheda all'altra utilizzando i tasti di scelta rapida, quando si chiude la finestra delle preferenze, NVDA non sarà in grado di capire che la finestra non esiste più.
Si tratta di un problema conosciuto di NVDA e non può essere risolto.


## Cambiamenti nella 4.0 ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## Cambiamenti nella 3.1 ##

* Viene utilizzato un nuovo metodo per intercettare il pulsante annulla e le
  schede. Ora non c'è bisogno di focalizzare tali elementi per usare i tasti
  rapidi.
* Quando viene modificata la scheda attiva, il focus viene spostato su di
  essa di modo che non appena viene premuto il tasto tab, si passi subito al
  primo elemento della scheda scelta.
* Nella finestra di dialogo delle preferenze, è ora possibile premere
  control + pagina su / giù per passare da una scheda all'altra. Ctrl + Tab
  e Ctrl + Maiusc +tab continuano a funzionare.
* Tutti i file manifest tradotti dovrebbero essere ora corretti.
* Correzioni minori.

## Cambiamenti nella 3.0 ##

* Correzioni varie nel file manifest.ini nel nome degli autori.
* Migliorato il rilevamento del menu di contesto quando viene premuto
  NVDA+Shift+d tre volte.
* Il pulsante Escape funziona soltanto se Dropbox e NVDA sono configurati
  per usare la stessa lingua.
* Diverse correzioni nel codice.
* Aggiunta/aggiornata la documentazione di tutti gli script.
* Nuove lingue: Arabo, brasiliano portoghese, Ceco, Dutch, Finlandese,
  Galiziano, Tedesco, Ungherese, Giapponese, Nepalese, Polacco, Russo,
  Spagnolo, Slovacco, Tamil, Turco.

## Cambiamenti nella 2.0 ##

* Nuove Lingue: Italiano
* La pressione del tasto rapido per tre volte o più, quando ci si trova nel
  menu di contesto, non causa più alcun problema.

## Cambiamenti nella 1.0 ##

* Prima versione

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx
