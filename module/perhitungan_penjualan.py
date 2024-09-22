def laba_bersih(pendapatan_kotor, harga_jual):
    pendapatan_bersih = pendapatan_kotor - harga_jual
    return pendapatan_bersih

def profit(jumlah_produk, harga_jual, biaya_produksi):
    total_penjualan = jumlah_produk * harga_jual
    total_biaya = jumlah_produk* biaya_produksi
    return total_penjualan - total_biaya