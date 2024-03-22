# dropbox


## Bilgi:
* Geliştiriciler: Rui Fontes, Patrick ZAJDA, Filaos ve diğer katkıda bulunanlar
* NVDA uyumluluğu: 2019.3 veya Sonrası
* [Kararlı sürümü indirin][1]


## Açıklama:
Bu eklenti, sırasıyla bir veya iki kez basıldığında Dropbox durumunu duyurmak veya Dropbox'un sistem tepsisinde bulunan menüsünü açmak için bir kısayol ekler.

Kısayol NVDA+Alt+D'dir
Her zaman olduğu gibi bunu Girdi hareketleri iletişim kutusunda Dropbox kategorisinden değiştirebilirsiniz.



## Sürüm geçmişi


### 4.7 için değişiklikler
* NVDA 2022.1 ile uyumluluk
* Son Dropbox arayüzünde sorunlara neden olduğu ve Windows 8 Microsoft tarafından desteklenmediği için Dropbox uygulama modülünü kaldırıldı.

### 4.6 için değişiklikler
* NVDA 2021.1 uyumluluğunu belirtir.

### 4.4 için değişiklikler
* Python3 uyumluluğu
* Son eklenti şablonunu kullanılıyor.
* Appveyor ile oluşturulacak depo değişikliği
* Belgelerdeki yanlış ve kullanılmayan kısayollar düzeltildi
* Belgelerde sürüm bildirimine hala atıfta bulunan açıklama güncellendi.

### 4.0 için değişiklikler
* Shift+NVDA+D kısayolu değiştirildi: bir kez basılırsa Dropbox durumunu duyurur, iki kez basılırsa içerik menüsünü açar.
* Çeviriler güncellendi.
* Windows 8 metro uygulamasıyla ilgili sorunlar düzeltildi.
* Eklenti yardımı artık yardım menüsünde mevcut değil, bunun yerine eklenti yöneticisinde bulunuyor.
* Dropbox, kullanıcı arayüzünü sürümden sürüme değiştirdikçe, ayarlar iletişim kutusunun tüm özellikleri kaldırıldı.
* Dropbox durumunu öğrenme kısayolu, ses zayıflaması kısayoluyla çakışmayı
  önlemek için Alt+NVDA+D olarak değiştirildi.

### 3.1 için değişiklikler
* İptal düğmesini ve sayfa sekmesini almak için başka bir yol kullanın. Artık kısayolları kullanmadan önce onları odaklamamız gerekmiyor.
* Etkin sekmeyi değiştirirken odak sekme sayfasına taşınır, böylece sekmeye basıldığında önceki kullanılan sekmede kalmak yerine sekmenin ilk öğesi etkinleştirilir. artık etkinleştirilmemişse.
* Tercihler iletişim kutusunda artık sekmeler arasında geçiş yapmak için control+sayfa yukarı/aşağı tuşlarına basmak mümkün. Control+tab ve control+shift+tab hâlâ çalışıyor.
* Tüm yerelleştirilmiş manifest dosyalarının artık iyi durumda olması gerekir.
* Küçük düzeltmeler.

### 3.0 için değişiklikler
* Ana bildirim dosyasında küçük düzeltme (yazarlar doğru şekilde görüntüleniyor).
* Shift+NVDA+D'ye üç kez basıldığında içerik menüsü algılaması iyileştirildi.
* Escape düğmesi artık çalışıyor (yalnızca Dropbox NVDA'nın kullandığı dilde kullanıldığında).
* Kodda birçok düzeltme var.
* Tüm komut dosyalarının belgeleri eklendi/güncellendi.
* Yeni diller: Arapça, Brezilya Portekizcesi, Çekçe, Felemenkçe, Fince, Galiçyaca, Almanca, Macarca, Japonca, Nepalce, Lehçe, Rusça, İspanyolca, Slovakça, Tamilce, Türkçe.

### 2.0 için değişiklikler
* Yeni diller: İtalyanca
* İçerik menüsündeyken kısayola üç kez veya daha fazla basmak artık sorun yaratmıyor.

### 1.0 için değişiklikler
* İlk sürüm


[1]: https://github.com/ruifontes/dropbox/releases/download/2024.03.21/dropbox-2024.03.21.nvda-addon
