#modul perhitungan_angsuran_per_bulan_klien.py

#fungsi bunga anuitas
def bunga_anuitas(pinjaman, bunga):
    hari = 30
    tabungan = pinjaman * bunga * hari
    return tabungan

#fungsi bunga flat
def bunga_flat(pinjaman, bunga):
    bulan = 12
    suku_bunga = bunga/100
    
    pokok_pinjaman = pinjaman / bulan
    bunga_pertahun = pinjaman * suku_bunga
    bunga_perbulan = bunga_pertahun / bulan
    total_angsuran = print('Angsuran perbulan yang wajib dibayarkan Rp.{}'.format(int(pokok_pinjaman + bunga_perbulan)))
    
    return total_angsuran