def tampilkan_data(data):
    i = 1
    for key, value in data.items():
        print(i, key, ': ', value)
        i += 1
        
def hargarata(data):
    sum=0
    jumlah=0
    average=sum/len(data)
    for harga in data.values():
        sum+=harga
        jumlah+=1
    return sum/jumlah
buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

tampilkan_data(buah)
print('rata rata harga satuan adalah:', hargarata(buah))   
