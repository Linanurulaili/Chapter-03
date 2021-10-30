def luasSegitiga1(a,t):
    luas= a*t/2
    return luas
alas1= 10
tinggi1= 20
print('Luas segitiga dengan alas', alas1, 'dan tinggi', tinggi1, 'adalah', luasSegitiga1(alas1,tinggi1))
def luasSegitiga2(a,t):
    luas= a*t/2
    return luas
alas2= 15
tinggi2= 45
print('Luas segitiga dengan alas', alas2, 'dan tinggi', tinggi2, 'adalah', luasSegitiga2(alas2,tinggi2))
def jumlah(x,y):
    tot= x+y
    return tot
segitiga1=luasSegitiga1(alas1,tinggi1)
segitiga2=luasSegitiga2(alas2,tinggi2)
print('Luas total kedua segitiga tersebut adalah:', jumlah(segitiga1,segitiga2))
