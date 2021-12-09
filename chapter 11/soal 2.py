from datetime import *
myFile=open('dataPeminjaman.txt', 'a')
while True:
    kode=input('Masukkan Kode Member:')
    nama=input('Masukkan Nama Member:')
    judulBuku=input('Masukkan Judul Buku:')
    tglskrg=datetime.date(datetime.now())
    x=str(tglskrg)
    tglKembali=tglskrg+timedelta(days=7)
    y=str(tglKembali)
    data=kode+'|'+nama+'|'+judulBuku+'|'+x+'|'+y+'\n'
    myFile.write(data)
    lanjut=input('Mau Lanjut? (y/n): ')
    if lanjut in ('N', 'n'):
        break
myFile.close()
