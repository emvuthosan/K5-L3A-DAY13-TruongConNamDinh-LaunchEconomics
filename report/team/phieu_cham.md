# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): TruongConNamDinh (L3A)
- Nhóm được chấm: MyBloodyValentine (L3A), nhóm một người: Bùi Quang Hiếu (2A202603639) · repo `hieuwwww/K5-L3A-DAY13-MyBloodyValentine-LaunchEconomics`, chấm trên commit `515a995`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện cho noi_dia + hang_nang khớp số của chính nhóm (4.472 đ, 5.865 đ/yêu cầu, 4.599 đ có cố định, simulated). Nêu đủ con số bất lợi kèm cách xử lý: power 0,64 nếu tác động thật 5 điểm (Giám đốc vận hành ký chấp nhận), xem lại 100% là 0,98–1,03× (lộ trình giảm xem lại theo bậc), quoc_te 1,88× (loại khỏi pilot). 4 điều kiện có vai trò phụ trách, 3/4 có ngày 2026-12-20; không đạt thì No-go. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Phạm vi thu hẹp có lý do bằng số (quoc_te 1,88× và 27,3% thành công; doi_tac 0,85×). Hồ sơ, A3, A4, B3, B4, E2 có nhãn simulated, nhưng bảng B1 (9 dòng, ví dụ 6.787 đ) và B2 (6.543 đ) trong `bang_chi_phi.md` không có nhãn simulated, nên chưa đạt "nhãn ở mọi số giả lập". |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot, đối chứng chạy cùng lúc; n = 859/nhóm, DE 6,96, ghi rõ đánh đổi mức chênh 6 điểm. D1 khớp (1.251 · 3.103 · 1.000 · 300 · m ≥ 299). 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn, người có quyền dừng; ngưỡng an toàn +2 điểm so với đối chứng, trần 6% đã tính tới tỉ lệ mở lại 4,25%. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Mọi con số khớp số tham chiếu của hội đồng (lệch 0%) và đề xuất không bỏ qua con số bất lợi nào. Đồng ý Go có điều kiện cho pilot noi_dia + hang_nang, kèm các điểm cần sửa:
- Mục 1–4 của hồ sơ ghi người phụ trách là "Người kiểm số", "Người viết code": đó là vai trong nhóm làm bài, không phải vai trò có quyền quyết định ở LogiX-VN.
- Điều kiện 3 ghi "trong tuần đầu", chưa có ngày kiểm tra cụ thể.
- Mục 3 chỉ ghi 5.865 đ/yêu cầu, chưa ghi bằng 0,49× của 12.000 đ (simulated).
- Bảng lỗi chỉ có một người gắn nhãn nên chưa đo được đồng thuận (nhóm một người, đã ghi trung thực, không tự điền 20/20).
- Bảng B1, B2 cần thêm nhãn simulated.

**Một câu hỏi cho đội trình:** Chi phí cả hệ thống 5.865 đ/yêu cầu bằng bao nhiêu lần 12.000 đ, và đã cộng chi phí cố định 40 triệu đ/tháng chưa?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chi phí cả hệ thống 5.865 đ/yêu cầu ≈ 0,49 lần mức 12.000 đ/yêu cầu nếu nhân viên tự làm; con số này chưa cộng chi phí cố định 40 triệu đ/tháng. Chi phí cố định được tính riêng cho phạm vi pilot noi_dia + hang_nang: ở mức 45.000 yêu cầu/tháng, chi phí là 4.599 đ/việc thành công (simulated), đã gồm 1.185 đ chi phí cố định/việc. Hai số dùng phạm vi và mẫu số khác nhau, nên không cộng trực tiếp 1.185 đ vào 5.865 đ.

## Chuẩn bị trước khi chấm (nháp, không tính điểm)

> **Cần duyệt.** **Vũ đã duyệt:** các số tham chiếu bên dưới khớp output `lab13.py` (Vũ là người đối chiếu số hồ sơ nhóm bạn lúc duyệt chéo). **Hoàng duyệt:** checklist và câu hỏi gợi ý. Điểm, quyết định và lý do chỉ điền khi đã đọc hồ sơ nhóm được chấm.

Số tham chiếu là số của nhóm mình, tính bằng `src/lab13.py` (lệch ≤ 2% coi là khớp).

### Đề xuất khớp bằng chứng

- [ ] Hồ sơ có nêu chi phí mỗi việc thành công (của mình: 4.472 đ [simulated]) và chi phí cả hệ thống (0,49× của 12.000 đ [simulated]).
- [ ] Có nêu con số bất lợi: quoc_te 1,88×; xem lại 100% ≈ 0,98–1,03× [simulated]; power 0,64 nếu chọn mức chênh 6 điểm.
- [ ] Đề xuất là một trong ba (Go, Go có điều kiện, No-go); mỗi điều kiện có người phụ trách và ngày kiểm tra.

### Số giả lập và phạm vi

- [ ] Mọi số tính từ cột `_simulated` có nhãn simulated.
- [ ] Phạm vi được thu hẹp có lý do bằng số (của mình: loại quoc_te 1,88× và doi_tac 0,85×).
- [ ] Không có từ cấm ở quy tắc 5 của README.

### Pilot ra được quyết định

- [ ] Có năm số D1 (của mình: 1.251 · 3.103 · 1.000 · 300 · m ≥ 299).
- [ ] Cách chia có ít nhất 20 cụm mỗi nhóm, hoặc ghi rõ đánh đổi.
- [ ] Ngưỡng an toàn có tính đến tỉ lệ mở lại hiện tại (4,25% toàn mẫu, 3,97% trong phạm vi), không làm pilot dừng ngay tuần đầu.
- [ ] Ít nhất ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, có người có quyền dừng.

### Câu hỏi gợi ý cho đội trình

Lấy từ `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, chọn một.

- Chi phí mỗi việc thành công là bao nhiêu nếu tuần đầu phải xem lại 100%?
- Cách chia của nhóm có ít nhất 20 cụm mỗi nhóm không?
- Với tỉ lệ mở lại 4,25% hiện tại, ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?
