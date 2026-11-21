# Báo cáo cá nhân — DaoTruongVu-2A202603721

## 1. Thông tin thành viên

- Họ tên: Đào Trường Vũ
- MSSV: 2A202603721
- Email:
- Vai trong nhóm: người kiểm số (trước giải lao), người viết code (sau giải lao: D1, E1). Nhóm 3 người nên gộp vai, xem `PHAN_CONG.md`.

## 2. Phần việc phụ trách

- Kiểm số độc lập Nhiệm vụ A và B, điền `report/team/bang_chi_phi.md`.
- Viết phần D1 (cỡ mẫu) và E1 (ba chỉ số) trong `src/lab13.py`; tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại cho luật an toàn của `pilot_plan.yaml`.
- Điền `report/team/chi_so.md`: bảng E1, hai chỉ số tự đề xuất, danh sách event có `trace_id`, phần kiểm tra chéo chỉ số ↔ event.
- Soát cuối: nhãn `simulated`, từ cấm ở quy tắc 5, `pilot_plan.yaml` đọc được và không còn dấu `?`.

## 3. Đóng góp cụ thể

- Viết `src/kiem_so_vu.py`, tính lại A1–A4 và B1–B4 theo cách khác `mo_hinh` (lọc lần chạy bằng `merge` thay vì `isin`, tính B4 và mức hoà vốn trực tiếp), để đối chiếu với code của Nam.
- So hai bản: trùng mọi dòng (lệch 0%). Ví dụ: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu; B3 giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]); B4 xem lại 100% ra 11.743 đ = 0,98× (12.415 đ = 1,03× với 15,3 phút làm lại) [simulated].
- Trong `src/lab13.py` viết `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`, `nhiem_vu_d1`, `nhiem_vu_e1`, `in_nhiem_vu_d_e`. Kết quả D1: 1.251 · 3.103 (42 người mỗi nhóm > 40) · 1.000 · 300 · m ≥ 299 (DE 6,96); power 0,64 nếu tác động thật chỉ 5 điểm. Kết quả E1: 82,83% · 27,12% · 4,25% (3,97% trong phạm vi noi_dia + hang_nang).
- Merge phần A/B của Nam từ `main` vào nhánh `vu`, gộp xung đột ở khối `__main__` của `src/lab13.py` để file chạy từ đầu đến cuối.

## 4. Bằng chứng

- Nhánh `vu` trên repo nhóm: commit `5812a5b` (kiểm số, bảng chi phí, D1 + E1, chỉ số và event), commit merge `ee0a0fd`, cùng các commit soát cuối sau đó.
- File: `src/kiem_so_vu.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md` (E1, event, kiểm tra chéo), phần D1/E1 trong `src/lab13.py`.
- `cd src && python lab13.py` chạy hết, in ba phép thử ĐẠT, các bảng A–B, D1 và E1.

## 5. Công cụ AI đã dùng

- **Claude Code (Anthropic):** dùng để đọc đề và chia việc cho nhóm (`PHAN_CONG.md`), viết `src/kiem_so_vu.py`, phần D1/E1 trong `src/lab13.py`, điền `bang_chi_phi.md` và phần E1/event của `chi_so.md`, gộp xung đột khi merge.
- **Cách tự kiểm tra:**
  - Chạy `kiem_so_vu.py` và `lab13.py` và so từng dòng giữa hai bản, rồi so với số chữa trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch ≤ 2%).
  - Kiểm tra quy tắc "giảm một nửa = nửa mức tăng" ở B1 (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).
  - Giải tay câu D1e: 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 298,5 → 299.
  - Chạy `yaml.safe_load` trên `pilot_plan.yaml` và grep dấu `?`.

## 6. Tự đánh giá

...
