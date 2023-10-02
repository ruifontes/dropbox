# dropbox #

* Autori: Patrick ZAJDA <patrick@zajda.fr>, Filaos și alți contributori
* NVDA compatibility: NVDA 2019.1 or later
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltarre][2]

This plugin add a shortcut to announce Dropbox status or open the Dropbox
systray menu when pressed once or twice respectively.  It also enhances
DropBox item lists.

* Comandă rapidă: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Modificări aduse în versiunea 4.4 ##

* Compatibilitate cu Python 3
* Folosiți ultimul șablon al suplimentului
* Schimbare de depozit pentru ca suplimentul să fie construit cu Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the
  announcement of the version

## Modificări aduse în versiunea 4.0 ##

* Ghidul add-on-ului este disponibil în managerul de add-on-uri.
* Scurtătura care oferă informații cu privire la starea Dropbox-ului a fost
  schimbată la Alt+NVDA+D pentru a evita conflictul cu suportul atenuării
  auddio.

## Modificări aduse în versiunea 3.1 ##

* Utilizează un alt mod pentru a găsi butonul anulare și tabulatorul
  paginii. Acum nu mai e nevoie să le focalizezi înainte de a utiliza
  scurtăturile.
* Când modifici tabulatorul activ, focalizarea se mută la tabulatorul
  paginii, deci când apeși tab, primul element din tabulator este activat,
  deci nu mai e nevoie să stai la tabulatorul anterior utilizat chiar dacă
  el nu este încă activat.
* În dialogul de preferințe, este acum posibil să apeși Control+Pagină
  Sus/Jos pentru a te comuta între tabulatoare. Control+Tab și
  Control+Shift+Tab încă funcționează.
* Toate fișierele Manifest locale ar trebui să fie acum OK.
* Corecții minore.

## Modificări aduse în 3.0 ##

* Corecții minore la fișierul Manifest principal (autorii sunt afișați
  corect).
* Meniul context a fost îmbunătățit când apeși Shift+NVDA+D de trei ori.
* Butonul escape acum funcționează (doar când utilizezi Dropbox în aceiași
  limbă cu NVDA).
* Multe corecții în cod.
* A fost adăugată documentația actualizată la toate script-urile.
* Limbi noi: Arabă, Portugheză-Braziliană, Cehă, Finlandeză, Galiciană,
  Germană, Maghiară, Japoneză, Nepaleză, Poloneză, Rusă, Spaniolă, Slovacă,
  Tamilă, Turcă.

## Modificări aduse în versiunea 2.0 ##

* Limbi noi: Italiană
* Apăsând scurtătura de trei ori sau mai mult când ești deja în meniul
  context nu mai cauzează probleme.

## Modifăcri aduse în versiunea 1.0 ##

* Lansarea Inițială

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
