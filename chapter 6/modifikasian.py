from operation import *
a = 2
b = 4
c = 6
d = 7
e = 9
f = 10
g = 5
h = 12
i = 34
print('a.', a, '+', b, 'x', c, '-', b, '=', kurang(jumlah(a, kali(b, c)), b))
print('b. (', b, '+', d, ') x (', c, '-', e, ') =', kali(jumlah(b,d),kurang(c,e)))
print('c. (', f, '+', a, ') / (', d, '+', g, ') / (', h, '-', i, ') =', bagi(bagi(jumlah(f,a),jumlah(d,g)),kurang(h,i)))
