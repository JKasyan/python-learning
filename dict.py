__author__ = 'evgen'

d = {}
d = dict(name='Jenya', age=29)
k = d.keys()
v = d.values()
el = d.pop('name')

#
d = dict(first_name='John', second_name='Smith', age=29)
for key in d.keys():
    row = '{0:<12} : {1:>12}'.format(key, d[key])
    print(row)

sorted_keys = sorted(list(d.keys()))
for key in sorted_keys:
    row = '{0:<12} : {1:>12}'.format(key, d[key])
    print(row)

kv = list(d.items())
for x in kv:
    row = '{0:<12} : {1:>12}'.format(x[0], x[1])
    print(row)

for k in d:
    print('{0:<12} : {1:>12}'.format(k, d[k]))

#
del d['first_name']
d['profession'] = 'developer'

#
a = d['dfdf']
a = d.get('dfdf')

#
a = ['a', 'b', 'c']
b = [1, 2, 3]
d = dict(zip(a, b))
d = {k: v for (k, v) in zip(a, b)}
d1 = {c: c ** 2 for c in range(0, 6)}
d2 = dict.fromkeys([1, 2, 3], 0)
d3 = dict.fromkeys('Kiev', 1)