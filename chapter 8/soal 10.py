buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}
def tampilkan_data(data):
    i = 1
    for key, value in data.items():
        print(i, key, ': ', value)
        i += 1
tampilkan_data(buah)
total_semua = 0

while True:
   nambu=input('Nama buah yang dibeli:')
   totalkg=int(input('Berapa Kg:'))
   hartot=buah[nambu]*totalkg
   total_semua += hartot 
   print('Total harga:', hartot, '\n')
   pil=input('Beli buah yang lain (y/n)?')
   if pil in ('N', 'n'):
        print('Total semua harga           :', total_semua)
        break
