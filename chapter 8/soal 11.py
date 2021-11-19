line = '================================'
buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}
def tampilkan_data(data):
    i = 1
    for key, value in data.items():
        print(i, key, ': ', value)
        i += 1
tampilkan_data(buah)
while True:
    print(line)
    print('Menu:')
    print('A.Tambah data buah')
    print('B.Beli buah')
    print('C.Keluar')
    pilihan = input('Masukan pilihan: ')
    if pilihan == 'a' or pilihan == 'A':
        print(line)
        tambahdata=input('Nama Data buah yang akan ditambahkan:')
        if (tambahdata in buah):
            print('Buah', tambahdata, 'sudah ada dalam data')
        else:
            harga=int(input('Harganya (Rp):'))
            buah[tambahdata]=harga
        for key, value in buah.items():
            print(key, ': Rp', value)

    elif pilihan == 'b' or pilihan == 'B':
        print(line)
        nambu=input('Nama buah yang dibeli:')
        totalkg=int(input('Berapa Kg:'))
        hartot=buah[nambu]*totalkg
        print('Total harga:', hartot)
    elif pilihan == 'c' or pilihan == 'C':
        exit()
    else:
        print(line)
        print('INPUT TIDAK VALID!!')

