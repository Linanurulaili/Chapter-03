try:
    file=open('d:/data2.txt', 'r')
    sum=0
    for data2 in file:
        sum=sum+int(data2)
except ValueError:
    print(sum)
    
