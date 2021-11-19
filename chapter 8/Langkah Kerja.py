#Langkah 1
print('soal')
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('a=', a)
print('b=', b)
print('--------------------------------------------------------------------------')
#Langkah 2
a.insert(3, 10)
b.insert(2, 15)
#Langkah 3
a.append(4)
b.append(8)
print('Setelah ada sisipan angka')
print('a=', a)
print('b=', b)
print('--------------------------------------------------------------------------')
#Langkah 4
a.sort()
b.sort()
print('Setelah di sorting secara ascending ')
print('a=', a)
print('b=', b)
print('--------------------------------------------------------------------------')
#Langkah 5
c=a[0:8]
d=b[2:10]
print('c=', c)
print('d=', d)
print('--------------------------------------------------------------------------')
#Langkah 6
print('Penjumlahan elemen c dan d = e')
Hasil=[]
jumlah=[]
if len(c)==len(d):
    for i in range(len(c)):
        jumlah=c[i]+d[i]
        Hasil.append(jumlah)
    e=Hasil
    print('e=',e)
print('--------------------------------------------------------------------------')
#Langkah 7
print('perubahan list kedalam tuple')
myTuple=tuple(e)
print(myTuple)
print('--------------------------------------------------------------------------')
#Langkah 8
print('min=', min(e))
print('maks=', max(e))
print('Jumlah elemen E=', len(e))
print('--------------------------------------------------------------------------')
#Langkah 9
myString ='python adalah bahasa pemrograman yang menyenangkan'
print('myString=', myString)
print('--------------------------------------------------------------------------')
#Langkah 10
hurufpenyusun=set(myString)
print('Huruf penyusun=', hurufpenyusun)
print('--------------------------------------------------------------------------')
#Langkah 11
Datalist=list(hurufpenyusun)
print('Bentuk list=', Datalist)
print('--------------------------------------------------------------------------')
Datalist.sort()
print('sesudah di urutkan')
print('Urut=', Datalist)







