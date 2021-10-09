#input data
print("Penjalanan dari kota A ke kota B")
JarakKotaAkeB=int(input("jarak tempuh perjalanan:"))
KecepatanKotaAkeB=int(input("Dengan Kecepatan:"))
print("Perjalanan dari kota B ke kota C")
JarakKotaBkeC=int(input("jarak tempuh perjalanan:"))
KecepatanKotaBkeC=int(input("Dengan Kecepatan:"))
print("_____________________________________________________________")
#waktu perjalanan
print("Lama waktu sampai perjalanan kota A ke kota B")
WaktuKotaAkeB=(JarakKotaAkeB*1000)/(KecepatanKotaAkeB*1000/60)
print("waktu perjalanannya adalah:",round(WaktuKotaAkeB),"menit")
print("_____________________________________________________________")
print("Lama waktu sampai perjalanan kota B ke kota C")
WaktuKotaBkeC=(JarakKotaBkeC*1000)/(KecepatanKotaBkeC*1000/60)
print("waktu perjalanannya adalah:",round(WaktuKotaBkeC),"menit")
print("Istirahat Sejenak")
LamaIstirahat=float(input("lama istirahat:"))
print("_____________________________________________________________")
total=round(WaktuKotaAkeB+WaktuKotaBkeC+LamaIstirahat)
Jam=round(total/60)
Menit=total-Jam*60
print("Lama Perjalanan adalah",(Jam), "Jam",(Menit), "menit")
print("_____________________________________________________________")
#menghitung total keseleluruhan waktu
print("Waktu berangkat pukul:")
jam=float(input("jam:"))
menit=float(input("menit:"))
sampaijam=jam+Jam
sampaimenit=menit+Menit
print("_____________________________________________________________")
if (sampaimenit < 60):
    print("tiba pukul",(sampaijam),":",(sampaimenit))
elif(sampaimenit > 60):
    jm=sampaijam+1
    mnt=sampaimenit-60
    print("tiba pukul",(jm),":",(mnt))
    
