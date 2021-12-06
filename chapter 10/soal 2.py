myFile=open('dataMhs.txt', 'a')
while True:
    nim=input('Masukkan NIM:')
    nama=input('Masukkan Nama Mhs:')
    alamat=input('Masukkan Alamat:')
    data=nim+'|'+nama+'|'+alamat+'\n'
    myFile.write(data)
    lanjut=input('Mau Lanjut? (y/n): ')
    if lanjut in ('N', 'n'):
        break
myFile.close()

