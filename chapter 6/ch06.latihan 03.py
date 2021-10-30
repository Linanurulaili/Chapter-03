#permutasi
print('a. Permutasi')
n = int(input('Masukkan bilangan n:'))
r = int(input('Masukkan bilangan r:'))
def faktorial(x):
               if x == 1:
                   return 1
               elif x == 0:
                   return 1
               else:
                   return (x*faktorial(x-1))
hasil = (faktorial(n)/faktorial(n-r))
print('Hasil P(', n, ',', r, ')adalah:', hasil)

#combinasi
print('b. Kombinasi')
n = int(input('Masukkan bilangan n:'))
r = int(input('Masukkan bilangan r:'))
def faktorial(x):
               if x == 1:
                   return 1
               elif x == 0:
                   return 1
               else:
                   return (x*faktorial(x-1))
hasil = (faktorial(n)/faktorial(n-r)*faktorial(r))
print('Hasil C(', n, ',',  r, ')adalah:', hasil)
