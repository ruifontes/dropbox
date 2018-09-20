# dropbox #

* Tác giả: Patrick ZAJDA <patrick@zajda.fr>, Filaos và các cộng tác viên
  khác
* Tải về [phiên bản chính thức][1]

This plugin will add a shortcut to announce Dropbox status, version or open
the Dropbox systray menu.  Also page tabs working on the preferences dialog
with Ctrl+tab / Ctrl+Shift+Tab and Ctrl+PageUp/Down.  To conclude, make the
cancel button working with escape.

* Phím tắt: NVDA+Alt+D
* Ctrl+Alt+T thông báo thẻ đang hoạt động.

## Các vấn đề còn tồn tại ##

* If you switch between tabs using the shortcuts, when you'll close the preferences window, NVDA won't be able to know the windows doesn't exist anymore.
It is a known issue on NVDA and cannot be fixed.


## Các thay đổi cho 4.0 ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## Các thay đổi cho 3.1 ##

* Use another way to get cancel button and page tab. Now we don't have to
  focus them before using shortcuts.
* When changing the active tab, the focus move to the tab page so when
  pressing tab, the first item of the tab is activated instead of staying to
  the previous used tab even if it is not activated anymore.
* In the preferences dialog, it is now possible to press control+page
  up/down to switch between tabs. Control+tab and control+shift+tab still
  work.
* All localized manifest files should now be OK.
* Các sửa lỗi chính.

## Các thay đổi cho 3.0 ##

* Minor correction in the main manifest file (authors are correctly
  displayed).
* Improved context menu detection when pressing Shift+NVDA+D three times.
* The escape button now works (only when using Dropbox in the same language
  NVDA uses).
* A lot of corrections in the code.
* Added/updated documentations of all scripts.
* New languages: Arabic, Brazilian Portuguese, Czech, Dutch, Finnish,
  Galician, German, Hungarian, Japanese, Nepali, Polish, Russian, Spanish,
  Slovak, Tamil, Turkish.

## Các thay đổi cho 2.0 ##

* Ngôn ngữ mới: tiếng Ý
* Pressing the shortcut three times or more when already being in the
  context menu doesn't cause problem anymore.

## Các thay đổi cho 1.0 ##

* Phiên bản đầu tiên

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
