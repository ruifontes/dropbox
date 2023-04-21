# dropbox #

* Tác giả: Patrick ZAJDA <patrick@zajda.fr>, Filaos và các cộng tác viên
  khác
* NVDA compatibility: NVDA 2019.1 or later
* Tải về [phiên bản chính thức][1]
* tải về [phiên bản thử nghiệm][2]

Plugin này thêm một phím tắt để thông báo trạng thái của Dropbox hoặc mở
trình đơn của nó từ khay hệ thống khi bấm một hay hai lần.  Nó cũng cải
thiện các thành phần trong danh sách của DropBox.

* Phím tắt: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Các thay đổi cho 4.4 ##

* Đã tương thích với Python 3
* Dùng mẫu addon cuối cùng
* thay đổi kho dữ liệu để dựng với Appveyor
* Sửa lỗi và gỡ bỏ các lệnh không dùng đến trong tài liệu hướng dẫn
* Cập nhật mô tả trong tài liệu hướng dẫn mà vẫn tham khảo thông báo của
  phiên bản

## Các thay đổi cho 4.0 ##

* Đã có trợ giúp cho add-on từ trình quản lý Add-on.
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
* Các sửa lỗi phụ.

## Các thay đổi cho 3.0 ##

* Vài chỉnh sửa trong tập tin manifest chính (hiển thị đúng tên tác giả).
* Cải thiện khả năng nhận dạng trình đơn ngữ cảnh khi bấm  Shift+NVDA+D ba
  lần.
* Nút escape giờ đã hoạt động (chỉ khi dùng Dropbox bằng ngôn ngữ giống với
  ngôn ngữ của NVDA).
* Nhiều chỉnh sửa trong mã nguồn.
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
