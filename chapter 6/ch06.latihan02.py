def starFormation1(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print('')
print('')
def starFormation2(n):
    for i in range(n, 0,-1):
        for j in range(i):
            print('*', end='')
        print('')
print('')
starFormation1(4)
starFormation2(3)
