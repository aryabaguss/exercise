#fungsi bunga terendah
def bunga_terendah(saldo, bunga):
    hari = 30
    tahun = 365
    tabungan = saldo * ((bunga/100) * hari) / tahun
    
    return round(tabungan,2)


#fungsi bunga anuitas
def bunga_anuitas(pinjaman, bunga):
    hari = 30
    tabungan = pinjaman * (bunga/100) * hari
    
    return tabungan
