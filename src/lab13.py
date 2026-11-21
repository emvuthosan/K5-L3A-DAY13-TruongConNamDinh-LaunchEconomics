"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    raise NotImplementedError('VIẾT Ở ĐÂY')


# ---------- Nhiệm vụ D1 · Cỡ mẫu (Vũ) ----------
# Cho sẵn: baseline 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02.
ICC = 0.02


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức trong docs/du_lieu_va_cong_thuc.md)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m − 1) × ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc=ICC):
    """c cụm, mỗi cụm m yêu cầu: c × m ÷ DE, luôn nhỏ hơn c ÷ ICC."""
    return c * m / he_so_thiet_ke(m, icc)


def m_toi_thieu(n_can, c, icc=ICC):
    """Số yêu cầu tối thiểu mỗi cụm để c cụm đạt n_can hiệu dụng: c·m ≥ n·(1 − ICC + ICC·m)."""
    if c <= n_can * icc:
        return math.inf  # c ÷ ICC ≤ n_can: không cụm nào đủ lớn
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def nhiem_vu_d1(p1=0.70, p2=0.75, icc=ICC):
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    n = co_mau(p1, p2)                                    # a
    de75 = he_so_thiet_ke(75, icc)                        # b
    n_nv = math.ceil(n * de75)
    nguoi_moi_nhom = math.ceil(n_nv / 75)
    n6 = co_mau(p1, p1 + 0.06)                            # e
    m6 = m_toi_thieu(n6, 20, icc)
    power_5_voi_n6 = NormalIndPower().power(
        proportion_effectsize(p2, p1), nobs1=n6, alpha=0.05, ratio=1.0)
    return dict(
        a_n_moi_nhom=n,
        b_de_m75=de75, b_n_moi_nhom=n_nv, b_nguoi_moi_nhom=nguoi_moi_nhom,
        b_du_nguoi=2 * nguoi_moi_nhom <= 40,
        c_tran_20_nv=20 / icc, c_dat=20 / icc >= n,
        d_tran_6_depot=6 / icc,
        e_n_6_diem=n6, e_m_toi_thieu=m6, e_de=he_so_thiet_ke(m6, icc),
        power_khi_that_5_diem=power_5_voi_n6,
    )


# ---------- Nhiệm vụ E1 · Tính thử ba chỉ số (Vũ) ----------
def nhiem_vu_e1(reqs):
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    mo_lai = reqs['mo_lai_trong_7_ngay'] == 1
    pham_vi = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    return dict(
        chinh=(chinh.mean(), int(chinh.sum()), len(reqs)),
        dung_bo_qua_goi_y=(bo_qua.mean(), int(bo_qua.sum()), len(xem)),
        an_toan_mo_lai_7_ngay=(mo_lai.mean(), int(mo_lai.sum()), len(reqs)),
        an_toan_trong_pham_vi=(mo_lai[pham_vi].mean(), int(mo_lai[pham_vi].sum()), int(pham_vi.sum())),
    )


def in_nhiem_vu_d_e(reqs):
    print('\nD1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    d = nhiem_vu_d1()
    print(f"  a) Theo yêu cầu: {d['a_n_moi_nhom']:,} yêu cầu mỗi nhóm")
    print(f"  b) Theo nhân viên, m = 75: DE = {d['b_de_m75']:.2f} → {d['b_n_moi_nhom']:,} mỗi nhóm"
          f" → {d['b_nguoi_moi_nhom']} người mỗi nhóm, tổng {2 * d['b_nguoi_moi_nhom']}"
          f" {'≤' if d['b_du_nguoi'] else '>'} 40: {'đủ' if d['b_du_nguoi'] else 'không đủ'} người")
    print(f"  c) 20 nhân viên mỗi nhóm: tối đa {d['c_tran_20_nv']:,.0f} hiệu dụng"
          f" {'≥' if d['c_dat'] else '<'} {d['a_n_moi_nhom']:,}: {'đạt' if d['c_dat'] else 'không đạt'}")
    print(f"  d) 6 depot mỗi nhóm: tối đa {d['d_tran_6_depot']:,.0f} hiệu dụng")
    print(f"  e) Mức chênh 6 điểm: {d['e_n_6_diem']:,} mỗi nhóm; 20 người mỗi nhóm cần"
          f" m ≥ {d['e_m_toi_thieu']} yêu cầu mỗi người (DE {d['e_de']:.2f})")
    print(f"  Power nếu tác động thật chỉ 5 điểm mà n = {d['e_n_6_diem']}: {d['power_khi_that_5_diem']:.2f}")

    print('\nE1 · Ba chỉ số tính thử trên 1.200 yêu cầu')
    for ten, (ti_le, tu, mau) in nhiem_vu_e1(reqs).items():
        print(f'  {ten:24s} {ti_le:7.2%}  ({tu}/{mau})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # CP4 · Nhiệm vụ D1 (cỡ mẫu) và CP5 · E1 (ba chỉ số): Vũ.
    in_nhiem_vu_d_e(reqs)
