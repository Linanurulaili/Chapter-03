try:
    namafile = input("Masukkan nama file: ")

    file = open(namafile, "r")

    print('Isi dari file', namafile, 'adalah:\n')
    print(file.read())

except FileNotFoundError:
    print('File tidak ditemukan!!')
