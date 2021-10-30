def starFormation2(n):
    for i in range(n, 0,-1):
        for j in range(i):
            print('*', end='')
        print('')
starFormation2(4)
print('')
