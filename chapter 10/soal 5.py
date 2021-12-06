nama=open('dataFile.txt', 'r')
hasil=open('hasilFile.txt', 'w')
data= nama.readlines()
for i in range(len(data)):
    hilang=data[i].replace('\n', '')
    buang= hilang.split('|')
    hasil.write(str(int(buang[0])+int(buang[1]))+'\n')
nama.close()
hasil.close()
