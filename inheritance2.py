''' Parent Binatang '''

class Binatang():    
    def __init__(self,nama):
        self.nama = nama
        
    def __str__(self):
        return "Animal: "+self.nama
    
    def jalan(self):
        print('{} sedang berjalan'.format(self.nama))

class Kucing(Binatang):
    def __init__(self, nama, umur):
        Binatang.__init__(self, nama) # Menggunakan nama kelas, ada atribut self yang diberikan ke parent
        self.umur = umur

class Kelinci(Binatang):
    def __init__(self, nama, umur):
        super().__init__(nama) # Memanggil __init__ menggunakan fungsi super(), tidak perlu self
        self.umur = umur

class Sapi(Binatang):
    def suara(self):
        print('MoOOooOoo')    
        
class Ikan(Binatang):
    def __init__(self, nama, umur):
        super().__init__(nama)
        self.umur = umur
    
    def jalan(self):
        print('{} sedang berenang, ikan gabisa jalan'.format(self.nama))
        
        
''' End Parent Binatang'''


''' Parent Manusia'''
class Manusia:
    def __init__(self, ID, nama):
        self.ID = ID
        self.nama = nama

class Guru(Manusia):
    def __init__(self, ID, nama, tahun_pensiun):
        super().__init__(ID, nama) # memanggil __init__ parent dengan super()
        self.tahun_pensiun = tahun_pensiun
    
    def __str__(self):
        return 'Selamat jalan kepada guru NO.{} {}, sebagai pensiunan Tahun {}'.format(self.ID, self.nama, self.tahun_pensiun)
    
    def pensiun(self):
        print('Selamat jalan kepada guru NO.{} {}, sebagai pensiunan Tahun {}'.format(self.ID, self.nama, self.tahun_pensiun))
        
''' End Parent Manusia'''


hewan1 = Kucing("miu",3)
print(hewan1)
print(hewan1.nama)
print(hewan1.umur)

hewan2 = Kelinci('Butter', 6)
print(hewan2)
print(hewan2.nama)
print(hewan2.umur)

guru1 = Guru(200176, 'Sri', 2040)
print(guru1.ID)
print(guru1.nama)
print(guru1.tahun_pensiun)

hewan3 = Sapi('Sapiii')
hewan3.suara()

hewan4 = Ikan('Mas Koki', 1)
hewan4.jalan()

guru2 = Guru(200175, "Arif",2023)
guru3 = Guru(200176, 'Sri', 2040)

guru2.pensiun()
guru3.pensiun()

