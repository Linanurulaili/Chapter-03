print('_______________________STATUS KELULUSAN UJIAN MAHASISWA_______________________')
print('Syarat kelulusan adalah:')
print('-Tidak ada nilai yang kurang dari 60,dan')
print('-Nilai matematika nya harus diatas 70')
print('_________________________________________________________')
#input data
print('Input nilai mata pelajaran')
nama=(input('nama:'))
bindo=float(input('Masukkan nilai bahasa indonesia:'))
matematika=float(input('Masukkan nilai matematika:'))
ipa=float(input('Masukkan nilai IPA:'))
print('_________________________________________________________')
#mengetahui status kelulusan
if(bindo<0) or (bindo>100) or (matematika<0) or (matematika>100) or (ipa<0) or (ipa>100):
   print('maaf input ada yang tidak valid') 
elif(bindo >= 60) and (ipa >= 60) and (matematika > 70):
             print('Status kelulusan : Ananda', nama, 'mendapatkan predikat LULUS')
else:
    print('Status kelulusan : Ananda', nama, 'mendapatkan predikat TIDAK LULUS')
               
                  
