''' hitung luas dan keliling persegi panjang '''

def luas():
    panjang = float(input('Masukkan panjang persegi panjang: '))
    lebar = float(input('Masukkan lebar persegi panjang: '))
    hitung = panjang * lebar

    return hitung

def keliling():
    panjang = float(input('Masukkan panjang persegi panjang: '))
    lebar = float(input('Masukkan lebar persegi panjang: '))
    hitung = (2 * panjang) + (2 * lebar)

    return hitung