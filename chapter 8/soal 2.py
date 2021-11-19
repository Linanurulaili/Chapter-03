try:
    banyak = int(input('Berapa banyak bilangan yang ingin dimasukan: '))
    bil = []
    for i in range(banyak):
        angka = int(input('Masukkan Angka Ke-' + str(i+1) + ': '))
        bil = bil + [angka]
    def dataStat(bil):
        maks=max(bil)
        mins=min(bil)
        average=sum(bil)/len(bil)
        return[round(average), maks, mins]
    print('cari rata rata, max, mins dari:', bil)
    print('adalah', dataStat(bil))
except ValueError:
    print('INPUT BUKAN ANGKA!!')

    
