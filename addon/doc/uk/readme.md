# dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* NVDA compatibility: NVDA 2019.1 or later
* Завантажити [стабільну версію][1]
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

## Зміни у версії 4.0 ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## Зміни у версії 3.1 ##

* Використовуйте інший спосіб щоб отримати кнопку "Скасувати" або вкладку
  сторінки. Тепер не треба їх фокусувати перед використанням гарячих клавіш.
* When changing the active tab, the focus move to the tab page so when
  pressing tab, the first item of the tab is activated instead of staying to
  the previous used tab even if it is not activated anymore.
* У діалозі параметрів можна перемикатися між вкладками за допомогою
  комбінацій control+сторінка Вгору/control+сторінка Вниз. Крім того,
  комбінації control+tab/control+shift+tab працюють як і раніше.
* Усі локалізовані manifest-файли мають бути в порядку.
* Невеличкі виправлення.

## Зміни у версії 3.0 ##

* Невеличке виправлення у головному manifest-файлі (імена авторів тепер
  відображаються коректно).
* Поліпшено виявлення контекстного меню при потрійному натисканні
  Shift+NVDA+D.
* Клавіша ескейп зараз працює (лише за умови, якщо Dropbox використовує ту ж
  саму мову, що й NVDA).
* Низка виправлень у коді.
* Додано/оновлено документацію для усіх скриптів.
* Нові мови: арабська, Галісійська, іспанська, непальська, нідерландська,
  німецька, польська, португальська (Бразилія), російська, словацька,
  тамільська, турецька, угорська, фінська, чеська і японська.

## Зміни у версії 2.0 ##

* Нова мова: італійська
* Натискання гарячих клавіш три або більше разів під час перебування у
  контекстному меню більше не викликає проблем.

## Зміни у версії 1.0 ##

* Перший реліз

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
