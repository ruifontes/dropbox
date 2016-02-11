# dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* Download [stable version][1]

This plugin will add a shortcut to announce Dropbox status, version or open
the Dropbox systray menu.  Also page tabs working on the preferences dialog
with Ctrl+tab / Ctrl+Shift+Tab and Ctrl+PageUp/Down.  To conclude, make the
cancel button working with escape.

* Shortcut: NVDA+Alt+D
* Ctrl+Alt+T naznani aktivni zavihek

## Znane težave ##

* If you switch between tabs using the shortcuts, when you'll close the preferences window, NVDA won't be able to know the windows doesn't exist anymore.
It is a known issue on NVDA and cannot be fixed.


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

[1]: http://addons.nvda-project.org/files/get.php?file=dx
