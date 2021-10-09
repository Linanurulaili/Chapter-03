#import math
import math
#input data
JarakYangDibutuhkan=int(input("jarak yang di butuhkan:"))
JarakTempuh=int(input("jarak perjalanan yang di tempuh untuk 1 lt bbm:"))
KapasitasTangki=int(input("Kapasitas Tangki Mobil:"))
print("_____________________________________________________________")

#menghitung liter bbm dari jarak tempuh
TotalLiterBBM=JarakYangDibutuhkan/JarakTempuh
print("Total Liter BBM yang di butuhkan adalah:",(TotalLiterBBM),"Liter")
TotalMinimalIsiBBM=TotalLiterBBM/KapasitasTangki
print("Minimal Mengisi BBM Hingga Penuh adalah:",math.ceil(TotalMinimalIsiBBM),"Kali")

    

