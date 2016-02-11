# dropbox #

* Authors: Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors
* İndir [kararlı sürüm][1]

Bu eklenti dropbox durumunun, versiyonunun söylenmesi ve dropbox menüsünün
açılması için bir kısayol tuşu ekler.  Aynı zamanda, sekme sayfaları
arasında geçiş için ctrl+tab, ctrl+shift+tab ya da ctrl+önceki sayfa,
ctrl+sonraki sayfa ve aktif sekme sayfasının söylenmesi için ctrl+alt+t
kısayol tuşları tanımlanmıştır.  Son olarak, escape tuşu iptal butonuna
basar.

* Shortcut: NVDA+Alt+D
* Ctrl+Alt+T aktif sekme sayfasını söyler.

## Bilinen sorunlar ##

* Eğer sekmeler arasında kısayol tuşlarıyla dolaşırsanız, tercihler iletişim kutusunu kapattığınızda, NVDA bunu bilemeyecektir.
Bu, NVDA hakkında bilinen bir problemdir ve çözümü bulunmamaktadır.


## 4.0 için değişiklikler ##

* Add-on help is available from the Add-ons Manager.
* The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid
  conflict with audio ducking support.

## 3.1 versiyonundaki değişiklikler ##

* Use another way to get cancel button and page tab. Now we don't have to
  focus them before using shortcuts.
* Aktif sekme değiştiğinde, odak sekme üzerine gelir. Dolayısıyla tab tuşuna
  basıldığında, sekmedeki ilk öge üzerine gelinebilir.
* Tercihler iletişim kutusunda, sekme sayfaları arasında dolaşmak için artık
  control+page up/down tuşlarına basabilirsiniz.
* Tüm yerelleştirilmiş manifest dosyaları artık sorunsuz olmalı.
* Küçük düzeltmeler.

## 3.0 versiyonundaki değişiklikler ##

* ana manifest dosyasında Küçük bir düzeltme (geliştiriciler doğru olarak
  gösteriliyor).
* Üç kez NVDA+Shift+D tuşllarına basıldığında içerik menüsünün açılışıyla
  ilgili iyileştirmeler.
* escape butonu şimdi çalışıyor (sadece NVDA ve Dropbox aynı dil arayüzüyle
  kullanılıyorsa).
* Kodla ilgili çok sayıda düzeltme.
* İşlevlerle ilgili eklenmiş ve güncellenmiş dokümantasyon.
* Yeni diller: Arapça, Brezilya Portekizcesi, Çekçe, Flemenkçe, Fince,
  Galiçyaca, Almanca, Macarca, Japonca, Nepalce, Lehçe, Rusça, İspanyolca,
  Slovakça, Tamil, Türkçe.

## 2.0 versiyonundaki değişiklikler ##

* Yeni diller: İtalyanca
* Dropbox menüsü açıkken kısayol tuşuna üç ya da daha fazla basılması sorun
  oluşturmuyor.

## 1.0 versiyonu ##

* İlk sürüm

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx
