# Parent Class
class Binatang():
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

# Child Class
class Anjing(Binatang):    # Child class (subclass) of Binatang
    pass

# Child Class
class Kucing(Binatang):    # Child class (subclass) of Binatang
    pass

# child class of Anjing
class Bulldog(Anjing):
    pass

# Class Manusia
class Manusia:
    def __init__(self, ID, nama):
        self.ID = ID
        self.nama = nama

# jalankan code di bawah ini
instance_hewan = Anjing("Pumpkin Pie",4)
print(instance_hewan.nama)
print(instance_hewan.umur)

instance_hewan_2 = Bulldog("rambo",9)
instance_hewan_2.nama

# Class Guru
# isi titik - titik di bawah ini

class Guru(Manusia):
    pass

# Buatlah objek atau instance guru1 dan sesuaikan dengan perintah di atas
# isi titik - titik di bawah ini

teacher = Guru(200175, 'Arif')
print(teacher.ID)
print(teacher.nama)

