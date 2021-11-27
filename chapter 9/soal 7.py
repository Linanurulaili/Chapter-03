data = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
        'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
        'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print('=' * 65)
print('NIM'.ljust(10),'NAMA MAHASISWA'.ljust(20),'TANGGAL LAHIR'.ljust(20),'ALAMAT'.ljust(20))
print('=' * 65)
for tabel in data:
    split_tabel = tabel.split(':')
    space = 11
    for x in range(len(split_tabel)):
        if x == 2:
            tanggal = split_tabel[x].split('-')
            tanggal.reverse()
            print('/'.join(tanggal).ljust(space), end='')
            continue
        print(split_tabel[x].ljust(space), end='')
        space= 21        
    print('')
print('-' * 65)
