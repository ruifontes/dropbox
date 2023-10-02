# dropbox #

* مطورو الإضافة: Patrick ZAJDA, Filaos وآخرون
* NVDA compatibility: NVDA 2019.1 or later
* تحميل [الإصدار النهائي][1]
* Download [development version][2]

This plugin add a shortcut to announce Dropbox status or open the Dropbox
systray menu when pressed once or twice respectively.  It also enhances
DropBox item lists.

* مفتاح الاختصار : NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Changes for 4.4 ##

* Python 3 compatibility
* Use the last addon template
* Repository change to be built with Appveyor
* Fixed wrong and removed unused shortcuts in the documentation
* Update the description in the documentation which still referenced the
  announcement of the version

## تعديلات الإصدار 4.0 ##

* إتاحة مساعدة للإضافة من مدير الإضافات البرمجية.
* تم تغيير اختصار الإعلان عن حالة dropbox ليصبح Alt+NVDA+D لتجنب التعارض مع
  اختصار دعم خفض الأصوات الأخرى.

## تعديلات الإصدار 3.1 ##

* استخدام طريقة أخرى للحصول على زر الإلغاء وتحديد التبويب المراد. حيث لم نعد
  في حاجة إلى تنشيطهم قبل استخدام مفاتيح الاختصار.
* بتغيير التبويب النشط, سينتقل المؤشر إلى التبويب لذا فعند ضغط مفتاح tab,
  سيتم تنشيط أول عنصر بالتبويب المختار بدلا من البقاء في نفس التبويب الذي
  كان مستخدم مسبقا حتى لو كان غير نشط.
* أصبح من الممكن التحرك بين تبويبات محاورة التفضيلات ببرنامج دروببوكس
  باستخدام control+page up/down. كما أن مفاتيح الاختصار Control+tab and
  control+shift+tab ما زالت تعمل.
* ينبغي أن تكون جميع ملفات الترجمة للغات الأخرى على ما يرام.
* تعديلات طفيفة

## تعديلات الإصدار 3.0 ##

* تعديلات طفيفة في ملف الإعلام الرئيسي (عرض أسماء مطوري الإضافة بطريقة
  صحيحة).
* تحسين حضور قائمة السياق عند الضغط على Shift+NVDA+D ثلاث مرات.
* عمل زر Escape (إذا استخدم DropBox نفس اللغة التي يستخدمها NVDA).
* مراجعة للشفرة البرمجية
* إضافة وتحديث لملفات المساعدة بكل الملاحق البرمجية.
* ترجمة الإضافة للغات: العربية, البرتغالية البرازيلية, الفنلندية, الغالية,
  الألمانية, المجرية, اليابانية, النيبالية, البولندية,الروسية, الإسبانية,
  السلوفاكية, التاميلية, التركية.

## تعديلات الإصدار 2.0 ##

* ترجمة الإضافة للغة الإيطالية
* بضغط الاختصار ثلاث مرات أو أكثر لم يعد يتسبب في حدوث مشكلات مرة أخرى

## تعديلات الإصدار 1.0 ##

* النسخة الأولى

[[!tag dev  stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
