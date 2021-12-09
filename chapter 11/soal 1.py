from datetime import *
def diffDate(x):
    skrg = datetime.now()
    a = str(skrg.year)+'-'+str(skrg.month)+'-'+str(skrg.day)
    tgl = datetime.strptime( a, '%Y-%m-%d')
    date = datetime.strptime( x, '%Y-%m-%d')
    y = date - tgl
    print(y.days)
    return y.days

diffDate('2021-12-11')

