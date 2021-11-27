data = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	{'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
for i in data:
    nilaiAkhir = (i['mid'] + (2 * i['uas'])) / 3
       
    i['nilaiAkhir'] = round(nilaiAkhir, 1)

    if nilaiAkhir >= 60:
        i['status'] = 'LULUS'
    else:
        i['status'] = 'TIDAK LULUS'
print('''
============================================================
|  NIM  |   NAMA   |  MID  |  UAS  |    NA    |   STATUS   |
============================================================''')
for x in range(len(data)):
    isi1=str(data[x] ['nim'])
    print('|  ' + isi1, end='')
    for y in range(7-2-len(isi1)):
        print(' ', end='')
    isi2=str(data[x] ['nama'])
    print('| ' + isi2, end='')
    for y in range(10-1-len(isi2)):
        print(' ', end='')
    isi3=str(data[x] ['mid'])
    print('|  ' + isi3, end='')
    for y in range(7-2-len(isi3)):
        print(' ', end='')
    isi4=str(data[x] ['uas'])
    print('|  ' + isi4, end='')
    for y in range(7-2-len(isi4)):
        print(' ', end='')
    isi5=str(data[x] ['nilaiAkhir'])
    print('|   ' + isi5, end='')
    for y in range(10-3-len(isi5)):
        print(' ', end='')
    isi6=str(data[x] ['status'])
    print('|   ' + isi6, end='')
    for y in range(12-3-len(isi6)):
        print(' ', end='') 
    print('|')
    
print('------------------------------------------------------------')
   
    
           
        
               
