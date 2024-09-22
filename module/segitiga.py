''' hitung luas dan keliling segitiga '''

def luas():
    alas = float(input('Masukkan alas segitiga: '))
    tinggi = float(input('Masukkan tinggi segitiga: '))
    hitung = alas * tinggi / 2

    return hitung

def keliling():
    sisi_1 = float(input('Masukkan sisi 1: '))
    sisi_2 = float(input('Masukkan sisi 2: '))
    sisi_3 = float(input('Masukkan sisi 3: '))
    hitung = sisi_1 + sisi_2 + sisi_3

    return hitung