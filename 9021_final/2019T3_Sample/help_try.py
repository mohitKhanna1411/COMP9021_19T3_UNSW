import numpy as np

a = np.arange(8)
b = a.reshape(4,2)
m = ['a','b','b','c','b']
n = ['b','b','c','b']
m.remove('b')
print('a',m)

if n in m:
    print('yes')

m.sort()
n.sort()
print(m+n)
if m == n:
    print('ok')
