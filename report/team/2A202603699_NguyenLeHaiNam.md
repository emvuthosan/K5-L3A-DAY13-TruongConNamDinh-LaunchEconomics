# Báo cáo cá nhân — NguyenLeHaiNam-2A202603699

## 1. Thông tin thành viên

- Họ tên: Nguyễn Lê Hải Nam
- MSSV: 2A202603699
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code trước giải lao (nhiệm vụ A, B) và người gắn nhãn 2 ở CP3. Nhóm 3 người nên gộp vai, xem `PHAN_CONG.md`.

## 2. Phần việc phụ trách

- `src/lab13.py`: ba hàm A1, `mo_hinh` (A2), tách theo loại (A3), chi phí cố định (A4), bảng độ nhạy B1–B4.
- `report/team/pilot_plan.yaml` (nhiệm vụ D).
- Bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- `report/team/group_report.md`, `report/team/phieu_cham.md`.
- Gắn nhãn độc lập 20 ca lỗi và cùng Hoàng điền bảng khắc phục trong `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- A1: ba phép thử đáp án biết trước đạt 1,20 · 1,25 · 1,25.
- A2: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Tử số tính mọi lần chạy kể cả lần lỗi; mẫu số chỉ đếm 978 yêu cầu `thanh_cong`.
- A3, A4: quoc_te 1,88× của 12.000 đ [simulated], lần 2 chỉ 11,4% ok nên chạy lại không giúp. Phạm vi noi_dia + hang_nang cộng chi phí cố định còn 4.599 đ = 0,38× [simulated].
- B: số ca làm lại là yếu tố nhạy nhất (+51,8%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ). Xem lại 100% cho 0,98×, hoặc 1,03× với 15,3 phút làm lại [simulated].
- D: chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm (m ≥ 299, DE 6,96), ghi rõ power 0,64 nếu tác động thật là 5 điểm. Ba luật dừng đủ bốn vế. Ngưỡng an toàn so với đối chứng kèm trần 6%, vì tỉ lệ mở lại hiện tại đã là 4,25%.
- E2: ba dòng rủi ro (làm lại gấp đôi, xem lại 100%, khối lượng thấp), số lấy từ bảng độ nhạy.

## 4. Bằng chứng

- Commit `a219bd2` (feat: pilot_plan), merge qua PR #2 từ nhánh `NguyenNam`: `src/lab13.py` phần A, B; `pilot_plan.yaml`; E2 trong `chi_so.md`; `group_report.md`.
- Chạy `cd src && python lab13.py`: in "Ba phép thử đáp án biết trước: ĐẠT" và các bảng A2, A3, A4, B1–B4.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích.

## 5. Công cụ AI đã dùng

- **Claude Code (Anthropic):** gợi ý code cho các hàm A1, `mo_hinh` và các kịch bản B; soạn nháp `pilot_plan.yaml`, bảng E2 và `group_report.md`; tạo nháp báo cáo này.
- **Cách tự kiểm tra:**
  - Ba phép thử A1 phải in ĐẠT.
  - Đối chiếu từng con số A, B, D với số chữa trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch ≤ 2%).
  - Kiểm tra quy tắc "giảm một nửa = nửa mức tăng" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).
  - Vũ tính lại độc lập bằng `src/kiem_so_vu.py`, lệch 0%.
  - Chạy `yaml.safe_load`, lệnh tìm dấu `?` và tìm từ cấm (quy tắc 5) trong `report/team`.
- Không dùng AI để gắn nhãn 20 ca lỗi ở CP3 hay để viết kết quả duyệt chéo.

## 6. Tự đánh giá

...
