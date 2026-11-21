# Team

## Thông tin nhóm

- Tên nhóm: truongconnamdinh
- Lớp: L3A 
- Repo nhóm: `K5-L3A-DAY13-TruongConNamDinh-LaunchEconomics` 
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đào Trường Vũ | 2A202603721 | 26ai.vudt@vinuni.edu.vn | emvuthosan | Người kiểm số (trước giải lao) · Người viết code (sau giải lao: D1, E1) |
|   2 | Nguyễn Lê Hải Nam | 2A202603699 | | | Người viết code (trước giải lao: A, B) · Người gắn nhãn 2 |
|   3 | Vũ Lê Hoàng | 2A202603542 | | | Người gắn nhãn 1 · kiêm giữ hồ sơ |

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

-

### Bằng chứng

-

## NguyenLeHaiNam-2A202603699

### Phần việc phụ trách

- Viết code A, B trong `src/lab13.py`; người gắn nhãn 2 (CP3); `report/team/pilot_plan.yaml`, `report/team/group_report.md`, `report/team/phieu_cham.md`

### Đóng góp cụ thể

-

### Bằng chứng

-

## DaoTruongVu-2A202603721

### Phần việc phụ trách

- Kiểm số và điền `report/team/bang_chi_phi.md`; viết code D1, E1 trong `src/lab13.py`; `report/team/chi_so.md`

### Đóng góp cụ thể

-

### Bằng chứng

-

## DaoTruongVu-2A202603721

### Phần việc phụ trách

- Người kiểm số trước giải lao (A, B); người viết code sau giải lao (D1, E1 trong `src/lab13.py`); `report/team/bang_chi_phi.md`, `report/team/chi_so.md` (E1, event, kiểm tra chéo); soát cuối nhãn `simulated` và từ cấm ở quy tắc 5.

### Đóng góp cụ thể

- Tính độc lập A1–A4, B1–B4 bằng `src/kiem_so_vu.py`, đối chiếu với `mo_hinh` của Nam: trùng mọi dòng (chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn [simulated]); điền toàn bộ `bang_chi_phi.md`.
- Viết `co_mau`, `he_so_thiet_ke`, `nhiem_vu_d1`, `nhiem_vu_e1` trong `src/lab13.py`: D1 ra 1.251 · 3.103 · 1.000 · 300 · m ≥ 299, power 0,64 ở mức 5 điểm; E1 ra 82,83% · 27,12% · 4,25%.
- Viết bảng chỉ số E1, 11 event có `trace_id` và kiểm tra chéo chỉ số ↔ event trong `chi_so.md`; duyệt số trong `group_report.md`, `phieu_cham.md` và event của bảng khắc phục trong `bang_loi.md`.
- Chia việc cho nhóm 3 người (`PHAN_CONG.md`); gộp xung đột khi merge phần A/B của Nam với D1/E1.

### Bằng chứng

- Nhánh `vu`, PR #3: commit `5812a5b`, `ee0a0fd`, `1d60cfe`, `ee80baf`; PR #1: commit `d6b63a0` (`PHAN_CONG.md`).
- Báo cáo cá nhân: `report/team/2A202603721_DaoTruongVu.md`.
