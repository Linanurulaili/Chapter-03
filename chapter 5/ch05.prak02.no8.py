from random import randint
i=0
while True:
    i+=1
    bil=randint(0, 10)
    print(bil)
    if bil == 5:
        break

print('jumlah perulangan:', i)
