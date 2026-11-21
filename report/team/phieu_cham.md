# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): TruongConNamDinh (L3A)
- Nhóm được chấm: ...

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | ... | ... |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | ... | ... |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | ... | ... |
| **Tổng** | | | | **... / 30** | |

**Quyết định của hội đồng:** Go · Go có điều kiện · No-go (giữ một)

**Lý do:** ...

**Một câu hỏi cho đội trình:** ...

**Câu trả lời của đội trình (ghi lại tại buổi):** ...

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
