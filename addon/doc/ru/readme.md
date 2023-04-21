# dropbox #

* Авторы: Patrick ZAJDA <patrick@zajda.fr>, Filaos и другие участники
* NVDA compatibility: NVDA 2019.1 or later
* Загрузить [стабильную версию][1]
* Download [development version][2]

This plugin add a shortcut to announce Dropbox status or open the Dropbox
systray menu when pressed once or twice respectively.  It also enhances
DropBox item lists.

* Горячая клавиша: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the
  announcement of the version

## Изменения в версии 4.0 ##

* Справка дополнения доступна в диспетчере дополнений.
* Горячая клавиша для выяснения состояния Dropbox была изменена на
  Alt+NVDA+D, чтобы исключить конфликт с поддержкой приглушения звуков.

## Изменения в версии 3.1 ##

* Используйте другой способ получить кнопку cancel и вкладку. Теперь мы не
  должны приводить их к фокусу перед использованием горячих клавиш.
* When changing the active tab, the focus move to the tab page so when
  pressing tab, the first item of the tab is activated instead of staying to
  the previous used tab even if it is not activated anymore.
* В диалоге настроек теперь можно нажать Ctrl+Page Up/Down для переключения
  между вкладками. Ctrl+ Tab и Ctrl+Shift+Tab всё ещё работает.
* Все локализованные файлы манифеста теперь должны быть в порядке.
* Мелкие исправления.

## Изменения в версии 3.0 ##

* Незначительная поправка в основном файле манифеста (авторы отображаются
  корректно).
* Улучшено обнаружение контекстного меню при нажатии Shift+NVDA+D три раза.
* Клавиша Escape Теперь работает  (только тогда когда Dropbox используется
  на томже языке который использует NVDA).
* Множество исправлений в коде.
* Добавлена / обновлена документация всех скриптов.
* Новые языки: Арабский, Бразильский Португальский, Чежский, Голландский,
  Финский, Галисийский, Немецкий, Венгерский, Японский, Непальский,
  Польский, Русский, Испанский, Словацкий, Тамильский, Турецкий.

## Изменения в версии 2.0 ##

* Новые языки: Итальянский
* Нажатие сочетания три или более раз , когда уже контекстное меню открыто,
  не вызывает более никаких проблем.

## Изменения в версии 1.0 ##

* Первый публичный релиз

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
