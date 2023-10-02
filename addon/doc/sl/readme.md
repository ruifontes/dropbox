# dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* NVDA compatibility: NVDA 2019.1 or later
* Download [stable version][1]
* Download [development version][2]

This plugin add a shortcut to announce Dropbox status or open the Dropbox
systray menu when pressed once or twice respectively.  It also enhances
DropBox item lists.

* Shortcut: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the
  announcement of the version

## Changes for 4.0 ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## Spremembe v  3.1 ##

* Use another way to get cancel button and page tab. Now we don't have to
  focus them before using shortcuts.
* When changing the active tab, the focus move to the tab page so when
  pressing tab, the first item of the tab is activated instead of staying to
  the previous used tab even if it is not activated anymore.
* In the preferences dialog, it is now possible to press control+page
  up/down to switch between tabs. Control+tab and control+shift+tab still
  work.
* Vse lokalizirane manifest datoteke bi morale sedaj biti v redu.
* Manjši popravki

## Spremembe v 3.0 ##

* Manjši popravek v glavni manifest datoteki (avtorji so pravilno
  prikazani).
* Izboljšana detekcija kontekstualnega menija ob trojnem pritisku
  Shift+MVDA+D
* Tipka Escape sedaj dela (samo takrat, ko je jezik DropBoxa in NVDA enak)
* Precej popravkov v kodi.
* Dodana/posodobljena dokumentacija vseh skript.
* Novi jeziki: Arabščina, Brazilska Portugalščina, Češčina, Nizozemščina,
  Finščina, Galicijščina, Nemščina, Madžarščina, Japonščina, Nepalščina,
  Poljščina, Ruščina, Španščina, Slovaščina, Tamilščina, Turščina.

## Spremembe v 2.0 ##

* Novi jeziki: Italijanščina
* Trokratni pritisk bližnjice ali več, ko se že nahajate v kontekstualnem
  meniju, ne povzroča več težav.

## Spremembe v 1.0 ##

* Osnovna Različica

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
