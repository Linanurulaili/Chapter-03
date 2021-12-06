myFile=open('isiFile.txt', 'r')
baca=myFile.readlines()
genap = 0
ganjil = 0
for i in baca:
    if int (i) % 2 == 0:
        genap += 1
        
    elif int(i) % 2 !=0:
        ganjil +=1
myFile.close()
print('Banyak bilangan genap=', genap)
print('Banyak bilangan ganjil=', ganjil)


