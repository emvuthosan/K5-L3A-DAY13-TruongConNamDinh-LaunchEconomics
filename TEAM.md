# Team

## Thông tin nhóm

- Tên nhóm: truongconnamdinh
- Lớp: L3A 
- Repo nhóm: `K5-L3A-DAY13-TruongConNamDinh-LaunchEconomics` 
- URL repo: https://github.com/emvuthosan/K5-L3A-DAY13-TruongConNamDinh-LaunchEconomics · Nhánh nộp: `main` · Commit chốt: (ghi khi push lần cuối)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đào Trường Vũ | 2A202603721 | | | Người kiểm số (trước giải lao) · Người viết code (sau giải lao: D1, E1) |
|   2 | Nguyễn Lê Hải Nam | 2A202603699 | | | Người viết code (trước giải lao: A, B) · Người gắn nhãn 2 |
|   3 | Vũ Lê Hoàng | 2A202603542 | 26ai.hoangvl2@vinuni.edu.vn| hoangtukhoi | Người gắn nhãn 1 · kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## VuLeHoang-2A202603542

### Phần việc phụ trách

- Người gắn nhãn 1 (CP3), giữ hồ sơ `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `TEAM.md`

### Đóng góp cụ thể

- Điền `TEAM.md`: vai sau khi gộp cho nhóm 3 người.
- `bang_loi.md`: chép 20 ca lỗi, gắn nhãn người 1, merge nhãn người 2 của Nam, đếm số ca lệch, viết quy tắc phân biệt; thống nhất nhãn ca 13 là Giới hạn hệ thống cho khớp quy tắc và bảng khắc phục.
- `ho_so_launch_v0.md`: điền bảy mục từ output `lab13.py`, `pilot_plan.yaml`, `chi_so.md`, `bang_loi.md`; chốt đề xuất **Go có điều kiện** với bốn điều kiện có người phụ trách và ngày kiểm tra, nêu cả con số bất lợi.
- `group_report.md`: đối chiếu số ở mục 4 với output `lab13.py`, điền đề xuất cuối, duyệt mục 5.
- Soát cuối: `yaml.safe_load` đọc được `pilot_plan.yaml`, không còn dấu `?`; không có từ cấm ở quy tắc 5; `python lab13.py` chạy hết.

### Bằng chứng

- Nhánh `hoang-2a202603542`: commit `04d7205`, `97dfc01`, `80f1fed`, `3505e5f`, `2cac438` và commit điền `TEAM.md`, `group_report.md`.
- Báo cáo cá nhân: `report/team/2A202603542_VuLeHoang.md`.

## NguyenLeHaiNam-2A202603699

### Phần việc phụ trách

- Viết code A, B trong `src/lab13.py`; người gắn nhãn 2 (CP3); `report/team/pilot_plan.yaml`, `report/team/group_report.md`, `report/team/phieu_cham.md`

### Đóng góp cụ thể

- `src/lab13.py` A1: ba hàm, ba phép thử đáp án biết trước ĐẠT (1,20 · 1,25 · 1,25).
- A2–A4: `mo_hinh` cho chi phí mỗi việc thành công 4.472 đ [simulated]; tách theo loại (quoc_te 1,88×); cộng chi phí cố định cho phạm vi noi_dia + hang_nang còn 4.599 đ = 0,38× [simulated].
- B1–B4: 9 kịch bản độ nhạy, cặp B2, giới hạn 1/2/3 lần chạy, xem lại 100% (0,98×, 1,03× với 15,3 phút làm lại) [simulated].
- `pilot_plan.yaml`: chú thích D1, D2; chia theo nhân viên 20 + 20, mde 6 điểm; ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- E2 trong `chi_so.md`: ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy.
- `bang_loi.md`: gắn nhãn người 2 độc lập; điền bảng khắc phục 5 ca (1, 20, 18, 13, 17), mỗi dòng có event, ngưỡng, vai trò phụ trách.
- `group_report.md`: viết mục 1–8, cập nhật mục C và đồng thuận 17/20 = 85%.
- `phieu_cham.md`: dựng khung chấm và checklist số tham chiếu; điểm và quyết định chờ buổi duyệt chéo 17:00.

### Bằng chứng

- Commit `a219bd2` (A, B, `pilot_plan.yaml`, E2, `group_report.md`; merge qua PR #2), `7fb7738` (nhãn người 2), `ba7b20d` (bảng khắc phục, cập nhật `group_report.md`).
- Báo cáo cá nhân: `report/team/2A202603699_NguyenLeHaiNam.md`.

## DaoTruongVu-2A202603721

### Phần việc phụ trách

- Kiểm số và điền `report/team/bang_chi_phi.md`; viết code D1, E1 trong `src/lab13.py`; `report/team/chi_so.md`

### Đóng góp cụ thể

-

### Bằng chứng

-
