# dropbox #

* 作者: Patrick ZAJDA, Filaos and other contributors
* Download [stable version][1]
* Download [development version][2]

このアドオンはDropboxの状態通知、バージョン通知、タスクトレイのメニューを開くショートカットを追加します。
また、Dropboxの設定ダイアログでは、タブを Ctrl+Tab, Ctrl+Shift+Tab, Ctrl+PageUp/PageDown
で移動できるようになり、エスケープでキャンセルのボタンを押せます。

* ショートカット: NVDA+Shift+D
* Ctrl+Alt+T 選択中のタブを通知する

## 既知の問題 ##

* ショートカットキーでタブを切り替えて、設定ウィンドウを閉じると、NVDAはウィンドウが閉じてしまったことを判断できません。これはNVDAの既知の問題で、修正できません。

## 4.0 での変更点 ##

* Translations update.
* Fixed issues with windows 8 metro app.

## 3.1 での変更点 ##

* キャンセルボタンとページタブを操作する方法を変更しました。ショートカットを実行する前にフォーカスを設定する必要がなくなりました。
* アクティブなタブを変更するときにフォーカスはそのタブに移動します。
  従って、Tab キーを押すと、フォーカスは移動する前のタブに残るのではなく、移動先タブの先頭項目に移動します。
* 設定ダイアログでは Ctrl+PageUp/PageDown
  でタブを切り替えられるようになりました。Ctrl+TabおよびCtrl+Shift+Tabも引き続き有効です。
* すべてのローカライズされたマニュフェストファイルで不具合が解決しました。
* 些細な修正を行いました。

## Changes for 3.0 ##

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

## Changes for 2.0 ##

* New languages: Italian
* Pressing the shortcut three times or more when already being in the
  context menu doesn't cause problem anymore.

## Changes for 1.0 ##

* Initial Release

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx

[2]: http://addons.nvda-project.org/files/get.php?file=dx-dev
