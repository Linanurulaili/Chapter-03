myFile=open('dataMhs.txt', 'a')
while True:
    nim=input('Masukkan NIM:')
    nama=input('Masukkan Nama Mhs:')
    alamat=input('Masukkan Alamat:')
    data=nim+'|'+nama+'|'+alamat+'\n'
    myFile.write(data)
    lanjut=input('Mau Lanjut? (y/n): ')
    if lanjut in ('N', 'n'):
        break
myFile.close()


bacaData= open('dataMhs.txt', 'r')
List=[]
data=bacaData.readlines()
for x in range(len(data)):
    pecah=data[x].split('|')
    Dict= {'nim': pecah[0], 'nama': pecah[1], 'alamat': pecah[2]}
    List.append(Dict)
print(List)
bacaData.close()
