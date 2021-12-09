from datetime import *
bacaData= open('dataPeminjaman.txt', 'r')
List=[]
data=bacaData.readlines()

def diffDate(x):
    skrg = datetime.now()
    a = str(skrg.year)+'-'+str(skrg.month)+'-'+str(skrg.day)
    tgl = datetime.strptime( a, '%Y-%m-%d')
    date = datetime.strptime( x, '%Y-%m-%d')
    y = tgl - date
    return y.days
denda=diffDate('2021-12-08')*2000
pinjam = date(2021, 12, 1)
maks = '2021-12-08'
for x in range(len(data)):
    pecah=data[x].split('|')
    Dict= {'kode member': pecah[0], 'nama': pecah[1], 'judul buku': pecah[2], 'mulai pinjam': pecah [3], 'pengembalian': pecah[4]}
    List.append(Dict)
    
kunci=input('Masukkan kode member yang mau dicari:')
print('===================================================================')
for i in range(len(List)):
    if kunci in List[i]['kode member']:
        print('Data Mahasiswa')
        print('-------------------------------------------------------------------')
        print('NIM               : ' +str(List[i]['kode member']))
        print('Nama              : ' +str(List[i]['nama']))
        print('Judul Buku        : ' +str(List[i]['judul buku']))
        print('Pinjam            :', pinjam)
        print('Maks Pengembalian :', maks)
        print('Pengembalian      :', datetime.date(datetime.now()))
        print('Terlambat         :', diffDate('2021-12-08'), 'hari')
        print('Denda             :', denda)
print('===================================================================')
if kunci not in List[0]['kode member']:
    if kunci not in List[1]['kode member']:
        if kunci not in List[2]['kode member']:
            print('\'data tidak di temukan\'')
    

bacaData.close()
        

