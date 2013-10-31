# dropbox #

* Authors: Patrick ZAJDA, Filaos and other contributors
* Download [stable version][1]
* Download [development version][2]

This plugin will add a shortcut to announce Dropbox status, version or open
the Dropbox systray menu.  Also page tabs working on the preferences dialog
with Ctrl+tab / Ctrl+Shift+Tab and Ctrl+PageUp/Down.  To conclude, make the
cancel button working with escape.

* 快捷键： NVDA+Shift+D
* Ctrl+Alt+T 朗读激活的标签。

## Known issues ##

* If you switch between tabs using the shortcuts, when you'll close the preferences window, NVDA won't be able to know the windows doesn't exist anymore.
It is a known issue on NVDA and cannot be fixed.

## Changes for 4.0 ##

* Translations update.
* Fixed issues with windows 8 metro app.

## Changes for 3.1 ##

* Use another way to get cancel button and page tab. Now we don't have to
  focus them before using shortcuts.
* When changing the active tab, the focus move to the tab page so when
  pressing tab, the first item of the tab is activated instead of staying to
  the previous used tab even if it is not activated anymore.
* In the preferences dialog, it is now possible to press control+page
  up/down to switch between tabs. Control+tab and control+shift+tab still
  work.
* All localized manifest files should now be OK.
* Minor corrections.

## 3.0的更新 ##

* 为完善的清单文件修正。
* 完善上下文菜单检测，可连续三次按下组合键“Shift+NVDA+D”实现。
* “退出”按钮有效（仅当 DropBox使用的语言与 NVDA相同时）。
* 许多代码的修正。
* 增加/更新所有脚本的文档。
* 新语言支持：包括阿拉伯语巴西葡萄牙语、捷克语、荷兰语、芬兰语、加利西亚与、德语、匈牙利语、日本语、尼泊尔语、波兰语、俄语、西班牙语、斯洛伐克语、坦尼耳语、
  土耳其语。

## 2.0的更新 ##

* 新语言：意大利语
* 当托盘菜单打开时，极使重复按下该快捷键多次也不会再产生任何故障。

## 1.0的更新 ##

* 初始版本

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx

[2]: http://addons.nvda-project.org/files/get.php?file=dx-dev
