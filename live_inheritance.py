class Jets:
    def __init__(self, asal, nama):
        self.asal = asal
        self.nama = nama
        
class A7S37(Jets):
    def __init__(self, asal, nama):
        super().__init__(asal, nama)

class IDN17(Jets):
    def __init__(self, asal, nama):
        super().__init__(asal, nama)
        

jet = A7S37('Swedia', 'AJS37')
print('Pesawat asal {} memiliki kode pesawat {}'.format(jet.asal,jet.nama))

jet2 = IDN17('Indonesia', 'IDN17')
print('Pesawat asal {} memiliki kode pesawat {}'.format(jet2.asal,jet2.nama))

print('====================================================================')

class Kendaraan:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        
class Mikrolet(Kendaraan):
    def __init__(self, kapasitas, tarif):
        super().__init__(kapasitas)  
        self.tarif = tarif
        
    def income(self):    
        pendapatan = self.kapasitas * self.tarif
        return pendapatan
    
class Bus(Kendaraan):
    def __init__(self, kapasitas, tarif):
        super().__init__(kapasitas)
        self.tarif = tarif
    
    def income(self):
        pendapatan = (self.kapasitas * self.tarif) + (self.kapasitas * self.tarif * 0.1)
        return pendapatan
    
angkot = Mikrolet(10, 2000)
print('Total Pendapatan = {:,}'.format(angkot.income()))

bus = Bus(30, 5000)
print('Total Pendapatan Bus = {:,}'.format(bus.income()))

print('====================================================================')

class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def display(self):
        print('Person Name = {}'.format(self.nama))
        print('Person Age  = {}'.format(self.umur))

class Student(Person):
    def __init__(self, nama, umur, peminatan):
        super().__init__(nama, umur)
        self.peminatan = peminatan
    
    def filter_umur(self):
        
        if self.umur > 18 and self.umur <= 24:
            kategori = 'Muda'
        elif self.umur > 24 and self.umur <= 45 :
            kategori = 'Produktif'
        else :
            kategori = 'Lanjut Usia'
        
        return kategori
    
    def display_student(self):
        print('Student Name         = {}'.format(self.nama))
        print('Student Age          = {}'.format(self.umur))
        print('Student Interest     = {}'.format(self.peminatan))
        print('Student Age Category = {}'.format(self.filter_umur()))
        
        
    

person1 = Person('Tomas Wild', 37)
person1.display()
print('-------------------------------')
student1 = Student('Albert', 23, 'Mathematics')
student1.display_student()

print('-------------------------------')
student2 = Student('Jonathan', 46, 'Science')
student2.display_student()

print('-------------------------------')
student3 = Student('Ronald', 25, 'Law')
student3.display_student()

print(student1.filter_umur())



        
