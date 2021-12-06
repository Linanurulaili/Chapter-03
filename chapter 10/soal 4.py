bacaData= open('dataMhs.txt', 'r')
List=[]
data=bacaData.readlines()
for x in range(len(data)):
    pecah=data[x].split('|')
    Dict= {'nim': pecah[0], 'nama': pecah[1], 'alamat': pecah[2]}
    List.append(Dict)
while True:
    kunci=input('Masukkan NIM yang mau dicari:')
    for i in range(len(List)):
        if kunci in List[i]['nim']:
            print('Data Mahasiswa')
            print('NIM   :' +str(List[i]['nim']))
            print('Nama  :' +str(List[i]['nama']))
            print('Alamat:' +str(List[i]['alamat']))
    if kunci not in List[0]['nim']:
        if kunci not in List[1]['nim']:
            if kunci not in List[2]['nim']:
                print('\'data tidak di temukan\'')
    ulang=input('Apakah ingin mengulang? (y/n):')
    if ulang in ('N', 'n'):
        break

bacaData.close()
        

    
                 

                 

                 





