from random import randint
angkarahasia = randint(0, 100)
print('=' *40)
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
print('=' *40)
score=100
while True:
    jawab=int(input('tebakan anda:'))
    if jawab==angkarahasia:
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break
    else:
        if jawab<angkarahasia:
            print('Hehehe… Bilangan tebakan anda terlalu kecil')
            score-=2
        else:
            print('Hehehe… Bilangan tebakan anda terlalu besar')
            score-=2
if(score>=0) and (score<=100):
    print('Score anda:' +str(score))
elif(score<0):
    print('Score anda:0')
    
