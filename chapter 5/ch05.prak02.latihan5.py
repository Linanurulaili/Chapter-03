from random import randint
angka_rahasia = randint(0, 100)
print('=' *40)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
print('=' *40)
while True:
    jawab=int(input('tebakan anda:'))
    if jawab==angka_rahasia:
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break
    else:
        if jawab<angka_rahasia:
            print('Hehehe… Bilangan tebakan anda terlalu kecil')
        else:
            print('Hehehe… Bilangan tebakan anda terlalu besar')
