def carinilaitertinggi(list):
    listnilaiakhir=[]
    for data in list:
        mid= data['mid']
        uas= data['uas']
        nilaiakhir= (mid+2*uas)/3
        listnilaiakhir+=[round(nilaiakhir, 1)]

        nomorindex=[]
        i=0
    for nilaiakhir in listnilaiakhir:
        tertinggi=max(listnilaiakhir)
        if nilaiakhir==tertinggi:
            nomorindex+=[i]
        i+=1

    for i in nomorindex:
        print('Nama:', list[i]['nama'],
              '('+list[i]['nim']+')',
              'dengan nilai akhir', listnilaiakhir[i])

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
carinilaitertinggi(nilaiMhs)

