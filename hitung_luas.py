from module import lingkaran, persegi_panjang, segitiga

choice = input('Apa yang ingin anda hitung (lingkaran / persegi panjang / segitiga): ')
choice2 = input('luas / keliling: ')

if choice == 'lingkaran':

    if choice2 == 'luas':
        print('Luas lingkaran adalah: {}'.format(lingkaran.luas()))

    elif choice2 == 'keliling':
        print('Keliling lingkaran adalah: {}'.format(lingkaran.keliling()))

    else:
        print('input anda salah!')

elif choice == 'persegi panjang':

    if choice2 == 'luas':
        print('Luas persegi panjang adalah: {}'.format(persegi_panjang.luas()))
    
    elif choice2 == 'keliling':
        print('keliling persegi panjang adalah: {}'.format(persegi_panjang.keliling()))

    else:
        print('input anda salah!')

elif choice == 'segitiga':

    if choice2 == 'luas':
        print('Luas segitiga adalah: {}'.format(segitiga.luas()))
    
    elif choice2 == 'keliling':
        print('Keliling segitiga adalah: {}'.format(segitiga.keliling()))

    else:
        print('input anda salah!')

else:
    print('Input anda salah!')

    