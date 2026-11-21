# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

> **Cần duyệt (xoá ghi chú này trước khi nộp).** **Vũ đã duyệt:** mọi con số ở mục 4 khớp `bang_chi_phi.md`, `chi_so.md` và output `lab13.py`, trừ dòng tỉ lệ đồng thuận (C): phải sửa theo `bang_loi.md` sau khi khôi phục hai bộ nhãn độc lập. **Hoàng duyệt:** mục 5 (cách gộp vai) và điền hai dòng còn chờ ở mục 4 (đề xuất cuối, kết quả hội đồng).

## 1. Thông tin nhóm

- Tên nhóm: TruongConNamDinh
- Lớp: L3A
- Thành viên: xem `TEAM.md` (3 người: Đào Trường Vũ, Nguyễn Lê Hải Nam, Vũ Lê Hoàng)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có cho chạy pilot hay không. Nhóm tính mọi con số bằng `src/lab13.py` trên mẫu 1.200 yêu cầu (1.624 lần chạy), đối chiếu từng nhiệm vụ với slide chữa (lệch ≤ 2%) trước khi dùng lại số cho nhiệm vụ sau. Người kiểm số (Vũ) tính lại độc lập toàn bộ A và B bằng `src/kiem_so_vu.py`, lệch 0% so với `lab13.py`. Dữ liệu là giả lập; mọi số tính từ cột `_simulated` ghi nhãn simulated.

## 3. Giải pháp

- **A · Chi phí mỗi việc thành công** ([bang_chi_phi.md](bang_chi_phi.md)): hàm `mo_hinh` cộng token + tool trên mọi lần chạy (kể cả lần lỗi) và phút xem lại, làm lại; chia cho số yêu cầu `thanh_cong`. Gọi lại theo từng `loai` (A3) và cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang (A4).
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` với 9 kịch bản đổi một yếu tố, một cặp, giới hạn 1/2/3 lần chạy (cộng 12.000 đ cho mỗi yêu cầu không thành công để ra chi phí cả hệ thống) và xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): Hoàng và Nam gắn nhãn độc lập 20 ca theo năm loại của Google PAIR, đồng thuận 17/20 = 85%; ghi quy tắc phân biệt cho 3 ca lệch (13, 16, 17). Bảng khắc phục chọn mỗi loại một ca (1, 20, 18, 13, 17), mỗi dòng có event, ngưỡng và một vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho ba cách chia trước khi chọn (`nhiem_vu_d1` trong `lab13.py`); chọn chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm; ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số tính thử bằng `nhiem_vu_e1` trong `lab13.py`, hai chỉ số tự đề xuất, 10 event có `trace_id` kèm kiểm tra chéo, ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy. Hồ sơ launch *(chờ người giữ hồ sơ)*.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Làm lại chiếm 51,8% và xem lại 40,7% tổng chi phí [simulated].
- Chi phí cả hệ thống (cộng 222 ca nhân viên làm thay) **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te **1,88×** [simulated]; quoc_te chạy lại không giúp (lần 1 đúng 30%, lần 2 chỉ 11,4%). Phạm vi pilot: noi_dia + hang_nang, cộng cố định còn 4.599 đ = 0,38× [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8% khi gấp đôi), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1% khi tăng 25%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ), khác giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần). Xem lại 100% cho 11.743 đ = 0,98× [simulated].
- Pilot: không cách chia theo cụm nào đủ mẫu cho 5 điểm với 40 nhân viên; chọn 20 + 20 nhân viên, mde 6 điểm (m ≥ 299, DE 6,96); power chỉ 0,64 nếu tác động thật là 5 điểm.
- Chỉ số trong đợt chạy thử (không có đối chứng, nên chưa nói được tác động của trợ lý): chỉ số chính 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại trong 7 ngày 4,25% (51/1.200), trong phạm vi noi_dia + hang_nang 3,97%.
- Tỉ lệ đồng thuận gắn nhãn (C): 17/20 = 85% (≥ 80%); ba ca lệch 13, 16, 17.
- Đề xuất cuối của `ho_so_launch_v0.md`: *(chờ người giữ hồ sơ chốt)*.
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: *(chờ buổi duyệt chéo 17:00)*.

## 5. Khó khăn và cách xử lý

- Nhóm chỉ có **3 người** cho 4 vai của lab, nên gộp vai: Hoàng là người gắn nhãn 1 kiêm giữ hồ sơ; Nam viết code trước giải lao (A, B) và là người gắn nhãn 2; Vũ kiểm số trước giải lao và viết code sau giải lao (D, E). Vẫn giữ đủ hai người gắn nhãn độc lập và đổi người viết code sau giải lao (chi tiết: `PHAN_CONG.md`).
- Đề nói "xem lại 5 phút, làm lại 9 phút" ở B4 nhưng dữ liệu cho trung bình 15,3 phút mỗi ca làm lại; nhóm ghi cả hai kết quả (0,98× và 1,03×) thay vì chọn con số có lợi.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; pilot phải thay bằng phút đo thật từ event `staff_review_decision` và `staff_rework_completed` sau tuần 1.
- Đợt chạy thử không có nhóm đối chứng, nên chỉ nói được "chỉ số trong đợt chạy thử là …", chưa nói được tác động của trợ lý.
- Mức chênh 6 điểm là đánh đổi: nếu tác động thật chỉ 5 điểm thì pilot có power 0,64, dễ kết luận nhầm là không có tác động.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, `NormalIndPower` và `proportion_effectsize` (mục `stats.power`)
- Tài liệu của lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
