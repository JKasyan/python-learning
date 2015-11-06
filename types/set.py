__author__ = 'evgen'

x = set('abcde')
y = set('bdxyz')

a = [1, 2, 3, 4, 5, 5]
z = set(a)

'e' in y

x - y
x | y
x & y
x ^ y
x > y, x < y

z = x.intersection(y) # x&y

for item in set('Jeka'):
    print(item)

S = set([1, 2, 3])
S | set([3, 4])

set([1, 2, 3]) == {1, 2, 3} #true

d = {}
type(d)

#
S = set()
S.add((1, 2, 3))
S.add([4, 5, 6]) # TypeError

S.add(set([1, 2, 3])) # TypeError: unhashable type: 'set'

S.add(frozenset([1, 2, 3]))


#
x = {i**2 for i in range(1, 11)}

#
managers = {'tom', 'sue'}
engineers = {'bob', 'sue', 'tom', 'vic'}

result = 'bob' in engineers
result = managers & engineers
result = engineers - managers
result = managers - engineers
result = engineers > managers
