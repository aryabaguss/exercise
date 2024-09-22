from module.bunga_bank import bunga_anuitas as anuitas
from module.bunga_bank import bunga_terendah
from module.perhitungan_penjualan import profit, laba_bersih

rendah = bunga_terendah(2000000, 10)
anuitass = anuitas(2000000,10)
prof = profit(150,35000, 100000)

print("Bunga terendah yang didapatkan = Rp {}".format(rendah))
print("Bunga Anuitas yang didapatkan = Rp {} ".format(anuitass))
print("Profit yang didapatkan = Rp {} ".format(prof))

