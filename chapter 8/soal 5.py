def kuadrat(bil):
    hasil=bil**2
    return hasil

data=[]
pangkat=[]
i=0
banyak = int(input('Berapa banyak bilangan yang ingin dimasukan: '))
while True:
    bil=int(input('Masukkan Angka Ke-' + str(i+1) + ': '))
    data.append(bil)
    banyak-=1
    i+=1
    pangkat.append(kuadrat(bil))
    if banyak==0:
        print('list data:', data)
        print('kuadratnya', pangkat)
        break
    
