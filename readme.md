[[!meta title="dropbox"]]

* Authors: Patrick ZAJDA, Filaos and other contributors
* NVDA compatibility: 2019.1 or later

This plugin add a shortcut to announce Dropbox status or open the Dropbox systray menu when pressed once or twice respectively.

* Shortcut: NVDA+Alt+D


## Changes for 4.7 ##

* Compatibility with NVDA 2022.1
* Remove Dropbox app module as it causes issues with last Dropbox interface and Windows 8 is not supported by Microsoft

## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the announcement of the version

## Changes for 4.0 ##

* Change Shift+NVDA+D behavior: if pressed once announce Dropbox status, twice open the context menu.
* Translations update.
* Fixed issues with windows 8 metro app.
* Addon help is no longer available in the help menu, it's found in the addons manager instead.
* As Dropbox changes his gui from version to version, all features for settings dialog were removed.
* Modified the shortcut to get dropbox status to Alt+NVDA+D to avoid conflict with audio ducking support.

## Changes for 3.1 ##

* Use another way to get cancel button and page tab. Now we don't have to focus them before using shortcuts.
* When changing the active tab, the focus move to the tab page so when pressing tab, the first item of the tab is activated instead of staying to the previous used tab even if it is not activated anymore.
* In the preferences dialog, it is now possible to press control+page up/down to switch between tabs. Control+tab and control+shift+tab still work.
* All localized manifest files should now be OK.
* Minor corrections.

## Changes for 3.0 ##

* Minor correction in the main manifest file (authors are correctly displayed).
* Improved context menu detection when pressing Shift+NVDA+D three times.
* The escape button now works (only when using Dropbox in the same language NVDA uses).
* A lot of corrections in the code.
* Added/updated documentations of all scripts.
* New languages: Arabic, Brazilian Portuguese, Czech, Dutch, Finnish, Galician, German, Hungarian, Japanese, Nepali, Polish, Russian, Spanish, Slovak, Tamil, Turkish.

## Changes for 2.0 ##

* New languages: Italian
* Pressing the shortcut three times or more when already being in the context menu doesn't cause problem anymore.

## Changes for 1.0 ##

* Initial Release

