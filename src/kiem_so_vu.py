"""Kiểm số độc lập (vai người kiểm số, Vũ) cho Nhiệm vụ A và B.

Không thay cho src/lab13.py: đây là bản tính riêng để đối chiếu với mo_hinh của người viết code.
Chạy trong src/: python kiem_so_vu.py
Mọi con số dùng cột *_simulated là số GIẢ LẬP, ghi nhãn simulated khi báo cáo.
"""
import pandas as pd

GIA_VAO, GIA_RA, GIA_TOOL, LUONG_PHUT, BASELINE = 26, 130, 15, 2000, 12000
CO_DINH_THANG, YC_THANG = 40_000_000, 45_000


# ---------- A1 · công thức đóng ----------
def lan_chay(p, k=None):
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def thanh_cong(p, k=None):
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so(p, k=None):
    return lan_chay(p, k) / thanh_cong(p, k)


# ---------- A2 · tính lại từ trace, viết theo cách khác mo_hinh ----------
def chi_phi(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong=LUONG_PHUT, xem=1.0, lam=1.0, max_lan=None):
    r = runs.merge(reqs[['request_id']], on='request_id')          # chỉ lần chạy của các yêu cầu này
    q = reqs.copy()
    if max_lan is not None:
        r = r[r.attempt <= max_lan]
        vuot = q.so_lan_chay > max_lan
        q.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        q.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    moi_lan = r.tokens_in * gia_vao / 1000 + r.tokens_out * gia_ra / 1000 + r.tool_calls * gia_tool
    token = (r.tokens_in * gia_vao / 1000 + r.tokens_out * gia_ra / 1000).sum()
    tool = (r.tool_calls * gia_tool).sum()
    xl = q.phut_xem_lai_simulated.sum() * luong * xem
    ll = q.phut_lam_lai_simulated.sum() * luong * lam
    tong = token + tool + xl + ll
    tc = int((q.ket_qua == 'thanh_cong').sum())
    return dict(token=token, tool=tool, so_tool=int(r.tool_calls.sum()),
                chay_lai=moi_lan[r.attempt > 1].sum(),
                phut_xl=q.phut_xem_lai_simulated.sum(), phut_ll=q.phut_lam_lai_simulated.sum(),
                xem_lai=xl, lam_lai=ll, tong=tong, thanh_cong=tc, so_yc=len(q),
                cps=tong / tc, hoa_don=(token + tool) / len(q),
                lan_chay_tb=len(r) / len(q))


def in_dong(ten, v, fmt='{:,.0f}'):
    print(f'  {ten:45s} {fmt.format(v)}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('A1 · ba phép thử (p = 0,8)')
    in_dong('tối đa 2 lần', lan_chay(0.8, 2), '{:.2f}')
    in_dong('chạy đến khi đúng', lan_chay(0.8), '{:.2f}')
    in_dong('hệ số chi phí, tối đa 3 lần', he_so(0.8, 3), '{:.2f}')

    print('\nA2 · toàn bộ mẫu')
    g = chi_phi(runs, reqs)
    for k in ['token', 'tool', 'so_tool', 'chay_lai', 'phut_xl', 'xem_lai', 'phut_ll', 'lam_lai',
              'tong', 'thanh_cong']:
        in_dong(k, g[k])
    in_dong('cps [simulated]', g['cps'])
    in_dong('hoá đơn token + tool / yêu cầu', g['hoa_don'], '{:,.1f}')
    in_dong('cps / hoá đơn (lần)', g['cps'] / g['hoa_don'], '{:.1f}')
    for k in ['lam_lai', 'xem_lai', 'token', 'tool']:
        in_dong(f'tỉ trọng {k} (%)', g[k] / g['tong'] * 100, '{:.1f}')
    in_dong('tỉ trọng giờ nhân viên (%)', (g['xem_lai'] + g['lam_lai']) / g['tong'] * 100, '{:.1f}')
    khong_tc = g['so_yc'] - g['thanh_cong']
    he_thong = (g['tong'] + khong_tc * BASELINE) / g['so_yc']
    in_dong(f'cả hệ thống / yêu cầu (+{khong_tc} ca × 12.000)', he_thong)
    in_dong('  so với 12.000 (lần)', he_thong / BASELINE, '{:.2f}')

    print('\nA3 · theo loại   n   tỉ lệ TC   lần chạy/yc   cps [sim]   ×12.000')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        m = chi_phi(runs, reqs[reqs.loai == loai])
        print(f'  {loai:10s} {m["so_yc"]:5d} {m["thanh_cong"] / m["so_yc"]:9.1%} {m["lan_chay_tb"]:12.2f}'
              f' {m["cps"]:11,.0f} {m["cps"] / BASELINE:8.2f}')
    ok = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d.status == 'ok')
    print('  tỉ lệ ok theo lần thử:')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3).to_string())

    print('\nA4 · cố định, phạm vi noi_dia + hang_nang')
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    m = chi_phi(runs, pv)
    in_dong('số yêu cầu / thành công', m['so_yc'])
    in_dong('', m['thanh_cong'])
    in_dong('tổng chi phí phạm vi [sim]', m['tong'])
    in_dong('cps phạm vi [sim]', m['cps'])
    for ten, he in [('đầy đủ', 1.0), ('một nửa', 0.5)]:
        tc_thang = YC_THANG * he * m['thanh_cong'] / len(reqs)
        cd = CO_DINH_THANG / tc_thang
        in_dong(f'{ten}: việc TC/tháng', tc_thang)
        in_dong(f'{ten}: cố định/việc', cd)
        in_dong(f'{ten}: cps + cố định', m['cps'] + cd)
        in_dong(f'{ten}: so với 12.000', (m['cps'] + cd) / BASELINE, '{:.2f}')

    print('\nB1 · độ nhạy')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(xem=2),
        'Xem lại giảm một nửa': dict(xem=0.5),
        'Làm lại gấp đôi': dict(lam=2),
        'Làm lại giảm một nửa': dict(lam=0.5),
        'Lương tăng 25%': dict(luong=2500),
        'Tối đa 2 lần chạy': dict(max_lan=2),
        'Chỉ 1 lần chạy': dict(max_lan=1),
        'B2 · token ×2 + xem lại ×2': dict(gia_vao=52, gia_ra=260, xem=2),
    }
    for ten, kw in kich_ban.items():
        c = chi_phi(runs, reqs, **kw)['cps']
        print(f'  {ten:30s} {c:8,.0f} {(c / g["cps"] - 1) * 100:+6.1f}%')

    print('\nB3 · giới hạn chạy, chi phí cả hệ thống')
    for k in [1, 2, 3]:
        m = chi_phi(runs, reqs, max_lan=k)
        ktc = m['so_yc'] - m['thanh_cong']
        print(f'  {k} lần: trợ lý {m["tong"]:12,.0f}  không TC {ktc:4d}  cả hệ thống'
              f' {m["tong"] + ktc * BASELINE:12,.0f}  cps {m["cps"]:7,.0f}')

    print('\nB4 · xem lại 100%, phạm vi noi_dia + hang_nang')
    ids_ok = set(runs.loc[runs.status == 'ok', 'request_id'])
    co_ok = pv.request_id.isin(ids_ok).sum()
    so_ll = (pv.ket_qua == 'lam_lai').sum()
    r_pv = runs[runs.request_id.isin(pv.request_id)]
    tt = (r_pv.tokens_in * GIA_VAO / 1000 + r_pv.tokens_out * GIA_RA / 1000 + r_pv.tool_calls * GIA_TOOL).sum()
    tc = (pv.ket_qua == 'thanh_cong').sum()
    ll_all = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated']
    in_dong('yêu cầu có ≥ 1 lần ok', co_ok)
    in_dong('ca lam_lai', so_ll)
    in_dong('token + tool', tt)
    in_dong('phút làm lại TB / trung vị (mọi ca lam_lai)', ll_all.mean(), '{:.1f}')
    in_dong('', ll_all.median(), '{:.1f}')
    for phut_ll in [9, ll_all.mean()]:
        tong = co_ok * 5 * LUONG_PHUT + so_ll * phut_ll * LUONG_PHUT + tt
        in_dong(f'làm lại {phut_ll:.1f} phút: tổng', tong)
        in_dong('  cps [sim]', tong / tc)
        in_dong('  so với 12.000', tong / tc / BASELINE, '{:.2f}')
        # hoà vốn: (co_ok * x * 2000 + phần còn lại) / tc = 12.000
        x = (BASELINE * tc - so_ll * phut_ll * LUONG_PHUT - tt) / (co_ok * LUONG_PHUT)
        in_dong('  phút xem lại hoà vốn', x, '{:.1f}')
