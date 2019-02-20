import random

a = 'eqwsdqweqwaqaq'
b = ''
x = len(a)
print(x)

for i in range(x-1):
    if a[i] == 'w' or a[i] == 'q':
        pass
    else:
        b = b+a[i]
print(a)
print(b)
