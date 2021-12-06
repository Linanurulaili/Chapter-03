nama=open('hasilTeks.txt', 'r')
hasil=open('teksHasil.txt', 'a')

myFile=nama.read()

mySet= set(myFile)

mySet.remove(' ')

myList=list(mySet)

myList.sort()


n=2

data = myFile.replace(myList[0], chr(ord(myList[0])-n))

i=1

while True:
    data=data.replace(myList[i], chr(ord(myList[i])-n))
    i+=1

    if i==10:
        break
    
data=data.replace(chr(63), chr(89))
data=data.replace(chr(64), chr(90))

print(data)
hasil.write(data)

nama.close()
hasil.close()

