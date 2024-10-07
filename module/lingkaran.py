''' hitung luas dan keliling lingkaran '''

from math import pi

def luas():
    jari = float(input('Masukkan jari-jari lingkaran: '))
    hitung = pi * jari * jari
    hitung  = round(hitung,3)

    return hitung

def keliling():
    r = float(input('Masukkan jari-jari lingkaran: '))
    hitung = 2 * pi * r
    hitung  = round(hitung,3)
    
    return hitung