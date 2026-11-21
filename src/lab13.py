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

CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng / tháng
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot đề xuất (A3, A4, B4)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    Thêm: chay_lai (token + tool của attempt > 1), hoa_don_moi_yc, khong_thanh_cong, ca_he_thong.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    khong_thanh_cong = len(reqs) - thanh_cong
    return dict(token=token, tool=tool,
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token + tool) / len(reqs),
                khong_thanh_cong=khong_thanh_cong,
                ca_he_thong=tong + BASELINE * khong_thanh_cong)


def bang(tieu_de):
    print(f'\n===== {tieu_de} =====')


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

    # ---------- A2 ----------
    bang('A2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps: simulated)')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    goc = ket_qua['cps']
    print(f'cps / hoá đơn mỗi yêu cầu: {goc / ket_qua["hoa_don_moi_yc"]:.1f} lần')
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua["tong"] * 100:5.1f}%')
    he_thong_moi_yc = ket_qua['ca_he_thong'] / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {ket_qua["khong_thanh_cong"]} ca × 12.000 đ): '
          f'{he_thong_moi_yc:,.0f} đ = {he_thong_moi_yc / BASELINE:.2f}× [simulated]')

    # ---------- A3 ----------
    bang('A3 · Theo loại yêu cầu (cps: simulated)')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"x12000":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        lan_chay = runs['request_id'].isin(r['request_id']).sum() / len(r)
        print(f'{loai:10s} {len(r):6d} {kq["thanh_cong"] / len(r) * 100:8.1f}% {lan_chay:7.2f} '
              f'{kq["cps"]:9,.0f} {kq["cps"] / BASELINE:6.2f}×')
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ lần chạy ok theo loại × attempt:')
    print((ok_theo_lan * 100).round(1).to_string())

    # ---------- A4 ----------
    bang('A4 · Cộng chi phí cố định, phạm vi noi_dia + hang_nang (simulated)')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    kq_pv = mo_hinh(runs, pv)
    print(f'Phạm vi: {len(pv)} yêu cầu, {kq_pv["thanh_cong"]} thành công, cps {kq_pv["cps"]:,.0f} đ')
    for nhan, khoi_luong in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = khoi_luong * kq_pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / tc_thang
        tong_viec = kq_pv['cps'] + co_dinh
        print(f'{nhan:20s} tc/tháng {tc_thang:9,.0f}  cố định/việc {co_dinh:7,.0f} đ  '
              f'cps + cố định {tong_viec:7,.0f} đ = {tong_viec / BASELINE:.2f}×')

    # ---------- B1 ----------
    bang('B1 · Đổi từng yếu tố (cps: simulated)')
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":28s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- B2 ----------
    bang('B2 · Giá token gấp đôi + xem lại gấp đôi (simulated)')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'{cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%)')

    # ---------- B3 ----------
    bang('B3 · Giới hạn số lần chạy (simulated)')
    print(f'{"k":>2s} {"tong_tro_ly":>12s} {"khong_tc":>9s} {"ca_he_thong":>12s} {"cps":>8s}')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        print(f'{k:2d} {kq["tong"]:12,.0f} {kq["khong_thanh_cong"]:9d} {kq["ca_he_thong"]:12,.0f} {kq["cps"]:8,.0f}')

    # ---------- B4 ----------
    bang('B4 · Xem lại 100%, phạm vi noi_dia + hang_nang (simulated)')
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    so_xem = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = kq_pv['token'] + kq_pv['tool']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'Yêu cầu có ≥1 lần chạy ok: {so_xem} · ca làm lại: {so_lam_lai} · token + tool: {token_tool:,.0f} đ')
    for nhan, phut_ll in [('làm lại 9 phút/ca', 9), (f'làm lại {phut_lam_lai_tb:.1f} phút/ca (TB dữ liệu)', phut_lam_lai_tb)]:
        tong = token_tool + so_xem * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT
        cps = tong / kq_pv['thanh_cong']
        hoa_von = (BASELINE * kq_pv['thanh_cong'] - token_tool - so_lam_lai * phut_ll * LUONG_PHUT) / (so_xem * LUONG_PHUT)
        print(f'{nhan:40s} tổng {tong:12,.0f} đ  cps {cps:7,.0f} đ = {cps / BASELINE:.2f}×  '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')

    # ---------- CP4 · D1 (cỡ mẫu) và CP5 · E1 (ba chỉ số): Vũ ----------
    in_nhiem_vu_d_e(reqs)
