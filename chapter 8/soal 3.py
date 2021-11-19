banyak = int(input('Berapa banyak nama yang ingin dimasukan? '))
name = []
for i in range(banyak):
    nama = str(input('Masukkan Nama Ke-' + str(i+1) + ': '))
    name = name + [nama]
    name.sort()
print('Nama yang anda masukkan adalah', name)
print('==============================================================')
for nama in name:
    print(nama, '(', len(nama), 'karakter)')


