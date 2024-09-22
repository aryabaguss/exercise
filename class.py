
class Kucing:
    jenis = "mamalia"
    kaki = 4
    suara = "meow"

    def __init__(self, nama, umur, ras, warna):
        self.nama = nama
        self.umur = umur
        self.ras = ras
        self.warna = warna

class Mobil:
    def __init__(self, merk, tipe_mesin):
        self.merk = merk
        self.tipe_mesin = tipe_mesin

class Segitiga:
    def __init__(self,alas,tinggi,tipe):
        self.alas = alas
        self.tinggi = tinggi
        self.tipe = tipe
        self.luas = 0.5 * alas * tinggi

class Persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        luas = self.panjang * self.lebar
        return luas
    
    def keliling(self):
        keliling = (2 * self.panjang) + (2 * self.lebar)
        return keliling

class Lingkaran:
    pi = 3.14
    atribut_kelas = 99
    def __init__(self,radius):
        self.radius = radius
        self.diameter = 2 * radius

    def keliling(self):
        keliling = self.pi * self.diameter
        return keliling
    
    def luas(self):
        luas = self.pi * self.radius ** 2
        return luas

class List_Angka:

    def __init__(self, number_list):
        self.number_list = number_list

    def filter_even(self):
        even = []

        for num in self.number_list:
            if num % 2 == 0:
                even.append(num)
        return even

class Angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek):
        return self.angka + objek.angka

# *** End of Class *** 


instance_segitiga = Segitiga(6,6,"siku")
type(instance_segitiga)

instance_segitiga.alas
instance_segitiga.tipe

segitiga_1 = Segitiga(alas=10, tinggi=3, tipe='sama kaki')
segitiga_2 = Segitiga(alas=20, tinggi=4, tipe='siku')

print('=================================')
print(segitiga_1.alas, segitiga_1.tinggi, segitiga_1.tipe, segitiga_1.luas)
print(segitiga_2.alas, segitiga_2.tinggi, segitiga_2.tipe, segitiga_2.luas)
print(type(segitiga_1))



persegi_panjang_1 = Persegi_panjang(5, 8)
persegi_panjang_2 = Persegi_panjang(15, 20)

print('=================================')
print(persegi_panjang_1.panjang)
print(persegi_panjang_2.panjang)



instance_lingkaran_1 = Lingkaran(7)
instance_lingkaran_2 = Lingkaran(3)

print('=================================')
print(instance_lingkaran_1.atribut_kelas, instance_lingkaran_2.atribut_kelas)
print(Lingkaran.atribut_kelas)

# bermutasi menjadi atribut instance, memiliki nilai sendiri
instance_lingkaran_1.atribut_kelas = 5

# nilai baru diupdate pada semua objek yang masih memiliki atribut kelas ini
Lingkaran.atribut_kelas = 28
print('=================================')
print(instance_lingkaran_1.atribut_kelas)
print(instance_lingkaran_2.atribut_kelas)
print(Lingkaran.atribut_kelas)

print('=================================')
instance_kucing_1 = Kucing('Minnie', 2, 'Persia', 'Coklat')
print(instance_kucing_1.suara)
print(instance_kucing_1.nama)

print('=================================')
lingkaran_1 = Lingkaran(7)
print('Luas lingkaran dengan radius {} = {}'.format(lingkaran_1.radius, lingkaran_1.luas()))
print('Luas lingkaran dengan radius {} = {}'.format(lingkaran_1.radius, lingkaran_1.keliling()))
      
print('=================================')
genap = List_Angka([1,2,3,4,5,6,7,8,9,10])
print(genap.filter_even())

print('=================================')
print('Luas persegi panjang dengan panjang lebar ({},{}) = {}'.format(persegi_panjang_1.panjang, persegi_panjang_1.lebar, persegi_panjang_1.luas()))
print('Keliling persegi panjang dengan panjang lebar ({},{}) = {}'.format(persegi_panjang_2.panjang, persegi_panjang_2.lebar, persegi_panjang_2.keliling()))

print('=================================')
angka_1 = Angka(10)
angka_2 = Angka(20)

print(angka_1 + angka_2)
print(angka_1.__add__(angka_2))