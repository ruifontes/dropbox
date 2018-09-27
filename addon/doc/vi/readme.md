# dropbox #

* Tác giả: Patrick ZAJDA <patrick@zajda.fr>, Filaos và các cộng tác viên
  khác
* Tải về [phiên bản chính thức][1]

Plugin này sẽ thêm phím tắt thông báo các thông tin của Dropbox như trạng
thái, phiên bản hay mở trình đơn Dropbox từ khay hệ thống.  Đồng thời, cũng
làm cho Ctrl+tab / Ctrl+Shift+Tab và Ctrl+PageUp/Down hoạt động được với các
thẻ trong hộp thoại preferences.  Làm cho nút cancel hoạt động được với
escape.

* Phím tắt: NVDA+Alt+D
* Ctrl+Alt+T thông báo thẻ đang hoạt động.

## Các vấn đề còn tồn tại ##

* Nếu chuyển giữa các thẻ bằng phím tắt, khi đóng cửa sổ preferences, NVDA không nhận biết được rằng cửa sổ đó không còn tồn tại nữa.
Đây là lỗi của NVDA và không thể khắc phục.


## Các thay đổi cho 4.0 ##

* Đã có trợ giúp cho add-on từ trình quản lý Add-ons.
* Phím tắt xem trạng thái của Dropbox đã thay đổi thành Alt+NVDA+D để tránh
  xung đột với lệnh giảm âm thanh.

## Các thay đổi cho 3.1 ##

* Dùng cách khác để nhận biết nút cancel và các thẻ. giờ chúng ta không cần
  phải c ó focus trước khi dùng phím tắt.
* Khi chuyển sang thẻ khác, con trỏ di chuyển đến danh sách các thẻ nên khi
  bấm tab, thành phần đầu tiên của thẻ được kích hoạt thay vì đứng ở thành
  phần của thẻ đã dùng trước đó, thậm chí khi nó không còn được kích hoạt
  nữa.
* Trong hộp thoại preferences, giờ đây đã có thể bấm control+page up/down để
  chuyển giữa các thẻ. Control+tab và control+shift+tab vẫn hoạt động.
* Tất cả các tập tin manifest được bản địa hóa giờ đây hoạt động tốt.
* Các sửa lỗi chính.

## Các thay đổi cho 3.0 ##

* Vài chỉnh sửa trong tập tin manifest chính (hiển thị đúng tên tác giả).
* Cải thiện khả năng nhận dạng trình đơn ngữ cảnh khi bấm  Shift+NVDA+D ba
  lần.
* Nút escape giờ đã hoạt động (chỉ khi dùng Dropbox bằng ngôn ngữ giống với
  ngôn ngữ của NVDA).
* Nhiều chỉnh sửa trong cho mã nguồn.
* Thêm / cập nhật tài liệu cho tất cả kịch bản.
* Các ngôn ngữ mới: Arabic, Brazilian Portuguese, Czech, Dutch, Finnish,
  Galician, German, Hungarian, Japanese, Nepali, Polish, Russian, Spanish,
  Slovak, Tamil, Turkish.

## Các thay đổi cho 2.0 ##

* Ngôn ngữ mới: tiếng Ý
* Bấm phím tắt ba lần trở lên khi đã đứng ở trình đơn ngữ cảnh không còn gây
  ra lỗi nữa.

## Các thay đổi cho 1.0 ##

* Phiên bản đầu tiên

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
