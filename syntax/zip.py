__author__ = 'evgen'

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = list(zip(L1, L2))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
D2 = {}
for (k, v) in zip(keys, values):
    D2[k] = v

D3 = dict(zip(keys, values))