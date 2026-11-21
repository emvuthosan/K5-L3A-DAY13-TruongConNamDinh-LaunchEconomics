# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); trong phạm vi noi_dia + hang_nang 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được nhân viên mở bằng trợ lý | Số yêu cầu nhóm can thiệp có `agent_suggestion_shown`, chia số `refund_request_created` có `arm` = can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra trong tuần | Không cần tính |

Ba chỉ số tính bằng `nhiem_vu_e1` trong `src/lab13.py`. Chỉ số chính trong đợt chạy thử là 82,83%.

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm (can thiệp/đối chứng), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), staff_id, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, het_lan_chay, ngoai_pham_vi…), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok/loi), trace_id | Khi ghi sổ cái |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- **Dùng · bỏ qua gợi ý:** `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`.
- **An toàn · lỗi lọt đến khách:** `ticket_reopened` trong 7 ngày kể từ `ticket_closed`, chia số `refund_request_created`.
- **Dùng · nhóm tự đề xuất:** `agent_suggestion_shown` theo staff_id, chia `refund_request_created` có arm = can thiệp.
- **An toàn · nhóm tự đề xuất:** `audit_sample_checked` có so_tien_da_hoan ≠ so_tien_dung, chia số đơn được kiểm tra.
- **Chi phí mỗi việc thành công** (luật dừng chi phí trong pilot): token và tool từ `agent_run_completed`, phút xem lại và làm lại đo thật từ `staff_review_decision` và `staff_rework_completed`, thay cho hai cột simulated.
- Cả năm chỉ số đều tính được từ danh sách event trên.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, từ 4.472 đ lên 6.787 đ [simulated] (yếu tố nhạy nhất, B1) | Tỉ lệ `lam_lai` theo tuần của nhóm trợ lý > 7% (đợt chạy thử: 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia; rà 20 trace làm lại gần nhất để tìm nguyên nhân gốc | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4); hoà vốn khi mỗi lần xem lại ≤ 5,1 phút | % yêu cầu được xem lại còn > 50% cuối bước rollout 0.25; phút xem lại trung vị > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; đo phút xem lại thật từ tuần 1 | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch: 33.750 việc/tháng ở quy mô đầy đủ) | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
