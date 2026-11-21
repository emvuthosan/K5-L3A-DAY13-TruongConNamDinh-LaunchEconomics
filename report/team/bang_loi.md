# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Năm loại lỗi (theo đề bài)

| Loại | Nghĩa là |
| --- | --- |
| Do người dùng | Người dùng nhập sai hoặc chọn sai |
| Hệ thống | Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách |
| Ngữ cảnh | Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không khớp hoàn cảnh của họ |
| Giới hạn hệ thống | Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý được |
| Ngầm | Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra |

## Hai mươi ca lỗi (chép nguyên văn từ đề bài)

| Ca | Mô tả |
| --: | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. |
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì. |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ". |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng. |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. |
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. |

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Vũ Lê Hoàng · Người gắn nhãn 2: Nguyễn Lê Hải Nam (gắn trong 8 phút, không trao đổi)

> Mỗi người gắn nhãn trên giấy hoặc file riêng trước, rồi mới chép vào bảng này. Không đọc mục "Bảng khắc phục" bên dưới hay đáp án tham khảo trong `docs/` trước khi gắn xong. Sau khi so thì không sửa hai cột nhãn độc lập.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | Do người dùng | ... | ... |
| 2 | ... | Hệ thống | ... | ... |
| 3 | ... | Ngữ cảnh | ... | ... |
| 4 | ... | Giới hạn hệ thống | ... | ... |
| 5 | ... | Ngầm | ... | ... |
| 6 | ... | Do người dùng | ... | ... |
| 7 | ... | Hệ thống | ... | ... |
| 8 | ... | Hệ thống | ... | ... |
| 9 | ... | Do người dùng | ... | ... |
| 10 | ... | Ngữ cảnh | ... | ... |
| 11 | ... | Giới hạn hệ thống | ... | ... |
| 12 | ... | Ngầm | ... | ... |
| 13 | ... | Giới hạn hệ thống | ... | ... |
| 14 | ... | Do người dùng | ... | ... |
| 15 | ... | Hệ thống | ... | ... |
| 16 | ... | Ngữ cảnh | ... | ... |
| 17 | ... | Ngầm | ... | ... |
| 18 | ... | Ngữ cảnh | ... | ... |
| 19 | ... | Giới hạn hệ thống | ... | ... |
| 20 | ... | Hệ thống | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

> *Nháp, cần duyệt.* **Hoàng duyệt:** nội dung khắc phục, vai trò phụ trách và ngưỡng của từng dòng. **Vũ duyệt:** tên event và thuộc tính khớp danh sách event trong `chi_so.md`, ngưỡng có đo được từ event đó không.
> Ba cột cuối soạn theo định nghĩa từng loại, chưa gắn với ca nào. Sau khi thống nhất nhãn, chọn mỗi loại một ca, điền cột "Ca" và sửa nội dung cho khớp ca đã chọn. Event lấy từ danh sách trong `chi_so.md`; `input_validation_failed` là event đề xuất thêm.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | Event `input_validation_failed` (trường sai định dạng, trace_id); tỉ lệ theo tuần, ngưỡng > 3% số yêu cầu | Kiểm tra định dạng ngay khi nhập, gợi ý cách sửa cụ thể và thêm bước xác nhận lại trước thao tác không đảo ngược được | Product designer luồng hoàn phí |
| ... | Hệ thống | `staff_review_decision` = sửa, hoặc `refund_ledger_write` có ket_qua = loi; theo dõi hằng ngày, ngưỡng ≥ 1 ca sai tiền mỗi ngày | Sửa tham số tool hoặc luật chính sách, thêm ca kiểm thử hồi quy; chặn trả lời "thành công" khi bước ghi chưa xác nhận | Tech lead trợ lý hoàn phí |
| ... | Ngữ cảnh | `ticket_reopened` có reason "khách hiểu khác kết quả" dù số tiền đúng; theo dõi hằng tuần, ngưỡng > 1% số yêu cầu đã đóng | Nêu rõ giả định và cách tính trong tin nhắn gửi khách; rà lại các mặc định của thiết kế với hoàn cảnh khách | PM trợ lý hoàn phí |
| ... | Giới hạn hệ thống | `handoff_to_staff` theo reason (thieu_du_lieu, ngoai_pham_vi, dinh_dang); theo dõi hằng tuần, ngưỡng > 10% số yêu cầu | Nói rõ trợ lý không xử lý được, chuyển nhân viên kèm tóm tắt; mở rộng dữ liệu hoặc định dạng nếu tỉ lệ cao kéo dài | Trưởng nhóm CSKH |
| ... | Ngầm | `audit_sample_checked` hằng tuần trên mẫu 100 đơn, ngưỡng > 1% đơn có `so_tien_da_hoan` khác `so_tien_dung` | Duy trì kiểm tra mẫu định kỳ; khi vượt ngưỡng, rà toàn bộ đơn cùng điều kiện và hoàn bù hoặc thu hồi | Kế toán trưởng |
