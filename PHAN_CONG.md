# Phân công công việc · Lab 13 (Nhóm 3 người: Hoàng, Nam, Vũ)

Lab được thiết kế cho 4 vai (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ). Nhóm có 3 người nên gộp vai, nhưng vẫn giữ ba yêu cầu bắt buộc:

- **Hai người gắn nhãn độc lập** ở CP3 (Hoàng và Nam).
- **Đổi người viết code sau giờ giải lao** (Nam → Vũ), để ít nhất hai người tự tay tính được chi phí.
- **Một người giữ hồ sơ** điền `ho_so_launch_v0.md` dần từ đầu buổi (Hoàng).

## 1. Vai chính

| Người | Vai | File chịu trách nhiệm chính |
| --- | --- | --- |
| **Hoàng** | Gắn nhãn 1, kiêm giữ hồ sơ và đọc đề (theo dõi điều kiện "Xong khi") | `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `TEAM.md` |
| **Nam** | Viết code trước giải lao (A, B), gắn nhãn 2 ở CP3 | `src/lab13.py` (phần A, B), `report/team/pilot_plan.yaml`, `report/team/group_report.md`, `report/team/phieu_cham.md` |
| **Vũ** | Kiểm số trước giải lao, viết code sau giải lao (D1, E1) | `report/team/bang_chi_phi.md`, `src/lab13.py` (phần D, E), `report/team/chi_so.md` |

## 2. Lịch theo checkpoint

| Mốc | Hoàng | Nam | Vũ |
| --- | --- | --- | --- |
| **14:00** · Cài đặt (10 phút) | Điền thông tin nhóm vào `TEAM.md`; mở sẵn khung `ho_so_launch_v0.md` | Cài venv, chạy thử `python lab13.py` | Cài venv trên máy mình (dùng để chạy kiểm tra trên máy khác lúc nộp) |
| **14:10** · CP1 · A (40 + 3 phút) | Đọc đề, nhắc quy tắc (nhãn `simulated`, không dùng từ cấm ở quy tắc 5 của README); ghi mục 1 và 3 vào hồ sơ | Viết 3 hàm A1, qua đủ 3 phép thử (1,20 · 1,25 · 1,25); viết `mo_hinh` (A2); chạy theo loại (A3); cộng chi phí cố định (A4) | Tính tay ít nhất một con số để đối chiếu (ví dụ 274,7 đ/yêu cầu hoặc 4.472 đ); điền bảng A1–A4 vào `bang_chi_phi.md` |
| **14:53** · CP2 · B (25 + 2 phút) | Ghi mục 2 (ba yếu tố nhạy nhất) vào hồ sơ | Viết vòng lặp 9 kịch bản B1, cặp B2, giới hạn chạy B3, xem lại 100% B4 | Điền bảng B1–B4; kiểm tra "giảm một nửa = nửa mức tăng"; viết câu trả lời B3, B4 (≤ 3 dòng, có số) |
| **15:20** · Giải lao | — | **Commit và push `src/lab13.py`** để chuyển cho Vũ | **Pull** `src/lab13.py` về máy mình |
| **15:35** · CP3 · C (30 + 3 phút) | Gắn nhãn 20 ca **độc lập**, ngồi riêng, 8 phút | Gắn nhãn 20 ca **độc lập**, ngồi riêng, 8 phút | Làm nốt phần B nếu còn; bắt đầu viết hàm `co_mau` cho D1 |
| | So nhãn với Nam, tính tỉ lệ đồng thuận (≥ 16/20), ghi quy tắc cho các ca lệch | Cùng Hoàng điền bảng khắc phục 5 ca (đủ 5 loại, mỗi dòng có cách phát hiện đo được và một vai trò phụ trách) | |
| **16:08** · CP4 · D (25 + 3 phút) | Chạy kiểm tra `yaml.safe_load` và lệnh tìm dấu `?`; ghi mục 6 vào hồ sơ | Điền `pilot_plan.yaml`: chú thích D1, D2, các trường, 3 luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ | Code 5 câu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299); tính tỉ lệ `mo_lai_trong_7_ngay` (4,25%) và đưa số cho Nam |
| **16:36** · CP5 · E (20 + 4 phút) | Hoàn thiện hồ sơ đủ 7 mục; viết dòng đề xuất cuối (Go / Go có điều kiện / No-go) | Viết bảng rủi ro kinh tế E2 (ít nhất 2 dòng, lấy số từ bảng độ nhạy) | Code 3 chỉ số E1; viết danh sách ít nhất 6 event có `trace_id` và phần kiểm tra chéo vào `chi_so.md` |
| **17:00** · Duyệt chéo Gate 2a (45 phút) | Trình bày hồ sơ nhóm mình (1 phút trình + 1 phút trả lời) | Viết `phieu_cham.md` chấm nhóm n + 1 | Đối chiếu số trong hồ sơ nhóm bạn, chuẩn bị câu hỏi cho đội trình |
| **17:45** · Đóng gói, nộp (15 phút) | Hoàn thiện `TEAM.md` (vai, đóng góp); chạy `python lab13.py` trên máy mình | Viết `group_report.md` | Chạy lệnh grep tìm từ cấm (quy tắc 5) trong `report/team` và soát nhãn `simulated` lần cuối |

## 3. Việc của từng người (checklist)

### Hoàng · Gắn nhãn 1, kiêm giữ hồ sơ

- [ ] Điền thông tin nhóm, thành viên, vai trong `TEAM.md`
- [ ] Điền `ho_so_launch_v0.md` dần từ đầu buổi: đủ 7 mục, mỗi mục có con số chính, trạng thái, người phụ trách (một vai trò)
- [ ] Gắn nhãn độc lập 20 ca lỗi (CP3), không trao đổi với Nam trước khi so
- [ ] Tính tỉ lệ đồng thuận, ghi quy tắc phân biệt cho các ca lệch trong `bang_loi.md`
- [ ] Kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?`
- [ ] Viết dòng đề xuất cuối hồ sơ, kèm điều kiện, người phụ trách và ngày kiểm tra
- [ ] Trình bày hồ sơ khi duyệt chéo
- [ ] Chạy `python lab13.py` trên máy mình để kiểm tra lần cuối

### Nam · Viết code (trước giải lao), gắn nhãn 2

- [ ] Viết 3 hàm A1, qua đủ 3 phép thử ĐẠT
- [ ] Viết `mo_hinh`, chạy A2, A3, A4
- [ ] Viết các kịch bản B1, B2, B3, B4 ở dòng `TODO CP2`
- [ ] Commit và push `src/lab13.py` lúc 15:20
- [ ] Gắn nhãn độc lập 20 ca lỗi (CP3), không trao đổi với Hoàng trước khi so
- [ ] Điền bảng khắc phục 5 ca trong `bang_loi.md` (cùng Hoàng)
- [ ] Điền `pilot_plan.yaml`: chú thích D1, D2, các trường, ít nhất 3 luật dừng đủ bốn vế
- [ ] Viết bảng rủi ro kinh tế E2 trong `chi_so.md`
- [ ] Viết `phieu_cham.md` khi làm hội đồng
- [ ] Viết `group_report.md`

### Vũ · Kiểm số (trước giải lao), viết code (sau giải lao)

- [ ] Tính tay ít nhất một con số để đối chiếu với code của Nam
- [ ] Điền `bang_chi_phi.md`: A1, A2, A3, A4, B1, B2, B3, B4 (ghi nhãn `simulated` cho các số giả lập)
- [ ] Pull `src/lab13.py` sau giải lao, viết phần D1 ở dòng `TODO CP4`
- [ ] Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại, đưa cho Nam đặt luật an toàn
- [ ] Code 3 chỉ số E1; điền bảng chỉ số, danh sách event (≥ 6, có `trace_id`) và phần kiểm tra chéo trong `chi_so.md`
- [ ] Đối chiếu số trong hồ sơ nhóm bạn khi duyệt chéo
- [ ] Soát cuối: không còn từ cấm ở quy tắc 5, mọi số giả lập có nhãn `simulated`

## 4. Việc chung của cả ba người

- [ ] Mỗi người copy `report/team/MSSV_HoTen.md` thành file riêng (ví dụ `report/team/20241234_NguyenVanAn.md`), ghi công cụ AI đã dùng và cách tự kiểm tra
- [ ] **Mỗi người tự nộp link repo trên LMS** trước 23h59 GMT+7 ngày lab (ai không nộp thì không có điểm)
- [ ] Mỗi người tự giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; cách tính cỡ mẫu hiệu dụng khi chia theo cụm; lý do của đề xuất cuối

## 5. Lưu ý

- Ghi rõ nhóm có **3 người** và đã gộp vai nào, trong `TEAM.md` và mục 5 của `group_report.md`.
- Hoàng và Nam **không mở** mục "Nhãn tham khảo cho 20 ca" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` trước khi gắn nhãn xong. Sau khi đã so thì không sửa bộ nhãn độc lập.
- Mỗi người commit file mình phụ trách để tránh xung đột. Riêng `src/lab13.py`: Nam sửa trước, Vũ sửa sau, chuyển qua lần push lúc giải lao.
- Không sửa hai file CSV; không commit `.venv/`, `.env`; không force-push.
