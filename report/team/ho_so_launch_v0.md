# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: truongconnamdinh · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công toàn mẫu (4.373.585 đ / 978 việc), gấp 16,3 lần hoá đơn token 274,7 đ/yêu cầu; xem lại + làm lại chiếm 92,5% [simulated] (nguồn: A2 trong `bang_chi_phi.md`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại gấp đôi +51,8% (6.787 đ) · 2) Tỉ lệ xem lại gấp đôi +40,7% (6.292 đ) · 3) Lương nhân viên +25% → +23,1% (5.506 đ); giá token gấp đôi chỉ +5,6% [simulated] (nguồn: B1, B2) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi noi_dia + hang_nang: 3.414 đ, cộng cố định 40 triệu/tháng = 4.599 đ = 0,38× so với 12.000 đ [simulated]. Loại quoc_te 22.515 đ = 1,88× (thành công 27,3%) nên loại khỏi phạm vi. Bất lợi: xem lại 100% thì 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) (nguồn: A3, A4, B4) | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200) · dùng (bỏ qua gợi ý) 27,12% (48/177) · an toàn (mở lại trong 7 ngày) 4,25% (51/1.200), trong phạm vi 3,97%; 10 event có `trace_id` (nguồn: `chi_so.md`) | Xong, có bằng chứng | Chuyên viên phân tích dữ liệu |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 17/20 = 85% (lệch ca 13, 16, 17, có quy tắc phân biệt); 5 cách khắc phục cho ca 1, 20, 18, 13, 17 đủ 5 loại, mỗi dòng có event và ngưỡng (nguồn: `bang_loi.md`) | Xong, có bằng chứng | Tech lead trợ lý hoàn phí |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20 + 20; mức chênh 6 điểm, 859 mỗi nhóm, m ≥ 299 yêu cầu/người (DE 6,96). Bất lợi: 40 người không đủ cho 5 điểm (tối đa 1.000 < 1.251), power 0,64 nếu tác động thật chỉ 5 điểm; 3 luật dừng (an toàn, chi phí, mức dùng) (nguồn: `pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98–1,03×, hoà vốn khi xem lại ≤ 5,1 phút; khối lượng còn một nửa → 5.784 đ = 0,48× [simulated] (nguồn: E2 trong `chi_so.md`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot phạm vi noi_dia + hang_nang ở 6 depot (không gồm quoc_te, doi_tac), ngày bắt đầu 2026-12-01, ngày quyết định 2027-01-05. Lý do: chi phí 0,38× so với nhân viên tự làm [simulated], nhưng lợi thế mất hết nếu phải xem lại 100% (0,98–1,03×) và pilot chỉ đủ mẫu cho mức chênh 6 điểm.

- Điều kiện 1: Sửa khoá chống trùng khi hoàn tiền (ca 20) và chặn báo "thành công" khi sổ cái chưa xác nhận (ca 7) · Người phụ trách: Tech lead trợ lý hoàn phí · Ngày kiểm tra: 2026-11-28
- Điều kiện 2: Ký chấp nhận mức chênh tối thiểu 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm) · Người phụ trách: Giám đốc vận hành · Ngày kiểm tra: 2026-11-28
- Điều kiện 3: Bật đủ 10 event có `trace_id`; thay phút xem lại và làm lại simulated bằng phút đo thật sau tuần 1 · Người phụ trách: Chuyên viên phân tích dữ liệu · Ngày kiểm tra: 2026-12-08
- Điều kiện 4: Có kế hoạch giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% không tiết kiệm (B4) · Người phụ trách: Trưởng nhóm CSKH · Ngày kiểm tra: 2026-12-15
