class Mobil:
    # initiate atribut kecepatan dan jarak
    def __init__(self, kecepatan, jarak):
        self.kecepatan = kecepatan
        self.jarak = jarak

class Motor:
    # initiate atribut kecepatan dan jarak, warna
    def __init__(self, kecepatan, jarak, warna):
        self.kecepatan = kecepatan
        self.jarak = jarak
        self.warna = warna

# buat class Skuter tanpa variabel dan method
class Skuter:
    pass

class Belanja:
    item1 = 'Roti'
    item2 = 'Soda'
    item3 = 'Selai'

    def __init__(self,qty1, qty2, qty3):
        self.qty1 = qty1
        self.qty2 = qty2
        self.qty3 = qty3

    def jumlah_belanja(self):
        print('Jumlah Belanja')
        print('{} = {}'.format(self.item1, self.qty1))
        print('{} = {}'.format(self.item2, self.qty2))
        print('{} = {}'.format(self.item3, self.qty3))

class AlatTulis:
    pensil = 2000
    pulpen = 3000
    penghapus = 1000

    def TotalHarga(self):
        print('Daftar Harga:')
        print('Pensil = {}'.format(AlatTulis.pensil))
        print('Pulpen = {}'.format(AlatTulis.pulpen))
        print('Penghapus = {}'.format(AlatTulis.penghapus))

class Pekerja:
    domain = '@company.com'

    def __init__(self, nama_depan, nama_belakang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
    
    def namalengkap(self):
        first_name = self.nama_depan.title()
        last_name = self.nama_belakang.title()

        print(first_name, last_name)

    def email(self):
        first_name = self.nama_depan.lower()
        last_name = self.nama_belakang.lower()

        print(f'{first_name}.{last_name}{self.domain}')

class Pelanggan:

    def __init__(self, kota, desa):
        self.kota = kota
        self.desa = desa
        self.kota_desa = print(f'{kota},{desa}')

class BankAccount:
    def __init__(self, nomor_rekening, nama, saldo):
        self.nomor_rekening = nomor_rekening
        self.nama = nama
        self.saldo = float(saldo)

    def setor_tunai(self,nominal):
        self.saldo += nominal

        

    def tarik_tunai(self,nominal):
        self.saldo -= nominal

    def display(self):
        print('Nomor Rekening = {}'.format(self.nomor_rekening))
        print('Nama Rekening  = {}'.format(self.nama))
        print('Saldo Rekening = Rp.{:,}'.format(float(self.saldo)))
    

'''
========== BATAS CLASS DAN MAIN CODE ==========
'''


porsche = Mobil(240,80)
print('Kecepatan dan jarak mobil porsche = {} Km/h {}Km'.format(porsche.kecepatan, porsche.jarak))

print('=================================')
supra = Motor(100, 10, 'Silver')
print('Kecepatan, jarak dan warna motor supra bapak = {} {} {}'.format(supra.kecepatan, supra.jarak, supra.warna))

print('=================================')
belanjaan = Belanja(3,5,2)
belanjaan.jumlah_belanja()

print('=================================')
daftar_harga = AlatTulis()
daftar_harga.TotalHarga()

print('=================================')
employee = Pekerja('arya', 'baGus')
employee.namalengkap()
employee.email()

print('=================================')
customer = Pelanggan('Malang', 'Landungsari')
customer.kota_desa

print('=================================')
account = BankAccount(2178514584, 'Mulyono', 5000000)
account.setor_tunai(250_000)
account.tarik_tunai(100_000)
account.display()

