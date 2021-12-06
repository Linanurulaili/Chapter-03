nama=open('isiTeks.txt', 'r')
hasil=open('hasilTeks.txt', 'a')

myFile=nama.read()

mySet= set(myFile)

mySet.remove(' ')

myList=list(mySet)

myList.sort(reverse=True)

n=2

data = myFile.replace(myList[0], chr(ord(myList[0])+n))

i=1

while True:
    data=data.replace(myList[i], chr(ord(myList[i])+n))
    i+=1

    if i==10:
        break
    
data=data.replace(chr(91), chr(65))
data=data.replace(chr(92), chr(66))

hasil.write(data)
nama.close()
hasil.close()


          
          

