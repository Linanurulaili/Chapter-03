print('Golongan A gaji pokok Rp.10.000.000,00 dengan potongan 2.5%')
print('Golongan B gaji pokok Rp.8.500.000,00 dengan potongan 2.0%')
print('Golongan C gaji pokok Rp.7.000.000,00 dengan potongan 1.5%')
print('Golongan D gaji pokok Rp.5.500.000,00 dengan potongan 1.0%')
#input data
kode=(input('Masukkan kode karyawan:'))
nama=(input('Masukkan nama karyawan:'))
gol=(input('Masukkan golongan karyawan:'))
gagol=float(input('Masukkan gaji golongan karyawan:'))
pot=float(input('Masukkan potongan persentase dari golongan karyawan(%):'))
hasil=gagol * (pot/100)
gaber=gagol - hasil
print('______________________________________________________________')
#tunjangan tunjangan
nikah=float(input('tunjangan suami/istri(%):'))
anak=float(input('tunjangan anak(%):'))
status=str(input('Masukkan status menikah:'))
if(status=='menikah'):
    jumlahanak=int(input('Masukkan jumlah anak:'))
    tjgnikah=1
if(status=='belum'):
    jumlahanak=0
    tjgnikah=0
print('______________________________________________________________')
#struk rincian
print('====================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------------------------')
print('Nama karyawan:', nama, '.')
print('Golongan:', gol, '.')
print('Status menikah:', status)
print('Jumlah anak:', jumlahanak)
print('-----------------------------------------------------------')
print('Gaji pokok:', gagol)
print('Potongan:', pot, '%')
print('-----------------------------------------------------------')
print('diskon: Rp.', float(hasil))
print('Gaji bersih:Rp.', float(gaber))
print('-----------------------------------------------------------')
tunjangannikah=(gagol*(nikah/100))*tjgnikah
print('Tunjangan istri/suami:', tunjangannikah)
tunjangananak=(gagol*(anak/100))*jumlahanak
print('Tunjangan anak:', tunjangananak)
gakot=gagol+tunjangannikah+tunjangananak
print('Gaji kotor:', gakot)
print('Potongan (', pot, '%):', hasil)
gabersih=gakot-hasil
print('Gaji bersih dengan tunjangan:', gabersih)

