#Harga rental mobil yang diberikan
print("____________________Rental Mobil Kusuma____________________")
Hargapokok=int(input("Harga sewa 12 jam pertama:Rp."))
Hargatambahan=int(input("Harga sewa setelah 12 jam per jamnya:Rp."))
print("_____________________________________________________________")

#Waktu sewa mobil yang dipakai
print("Waktu peminjaman:")
jam1=float(input("Jam:"))
menit1=float(input("menit:"))
print("Waktu pengemb3alian:")
jam2=float(input("Jam:"))
menit2=float(input("menit:"))
SelisihJam=jam2-jam1
SelisihMenit=menit2-menit1
print("Total waktu:",round(SelisihJam),"jam",round(SelisihMenit),"menit")
print("_____________________________________________________________")

#Pembayaran rental mobil
if(SelisihJam > 12):
    print("Harga sewa total:Rp.",round(Hargapokok+(Hargatambahan*(SelisihJam-12)+Hargatambahan*(SelisihMenit/60))))
elif(SelisihJam < 12):
    print("Harga sewa total:Rp.",round(Hargapokok/12*(SelisihJam)+(Hargapokok/12/60)*(SelisihMenit)))
else:
    print("Harga sewa total:Rp.",round(Hargapokok))
print("_____________________________________________________________")


