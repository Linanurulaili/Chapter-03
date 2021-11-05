n=0
sum=0
print("----------------------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("----------------------------------------")
while True:
    try:
        bil=int(input('masukkan bilangan bulat:'))
        n+=1
        sum=sum+bil
        lagi=input('Lagi (y/n)?:')
        if lagi=='n':
            rata=sum/n
            print('Rata-ratanya adalah:',rata)
            break
        elif lagi!='y':
            break
    except ValueError:
        print('Bukan bilangan bulat')
