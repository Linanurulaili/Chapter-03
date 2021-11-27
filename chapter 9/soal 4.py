import random
nama=input('Masukkan String yang akan diubah : ')
banyak=(int(input('Berapa Kali Perulangan? ')))
def shuffleString(x, n):
    data=[]
    while True:
        a=''.join(random.sample(x,len(x)))
        if a in data:
            continue
        else:
            data.append(a)
            n-=1
            if n==0:
                print(data)
                break
print('Random String(', nama,',', banyak,') ==> ', end='')
shuffleString(nama, banyak)
