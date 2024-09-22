# modul produksi untuk menghitung profit dan hpp produk

def profit(info):
    profit_sell = (info['jumlah_produk'] * info['harga_jual']) - (info['jumlah_produk'] * info['biaya_produksi'])
    print('Total profit bulan ini adalah: Rp.{}'.format(profit_sell))

def harga_pokok(info):
    # total_prod = (info['jumlah_produk'] - info['sisa_produk']) * info['biaya_produksi']
    total_prod = info['biaya_produksi'] +info['jumlah_produk'] - info['sisa_produk']
    print('Harga pokok yang dikeluarkan adalah: Rp.{}'.format(total_prod))