__author__ = 'evgen'

L1 = [1, 2, 3]
for i in range(len(L1)):
    L1[i] += 1

L1 = [i+1 for i in L1]

res = []
for x in L1:
    res.append(x + 1)

#
file = open('/home/evgen/pgadmin.log')
lines = file.readlines()
lines = [line.rstrip() for line in lines]

#
L2 = ['p', 1, 22]
L2 = [x**2 for x in L2 if not x == 'p']


#
F2 = open('/home/evgen/pgadmin.log')
L3 = F2.readlines()
L4 = [line for line in L3 if line[:5] == 'ERROR']

#
L5 = [x + y for x in 'abc' for y in 'def']
L6 = [x ** y for x in [1, 2, 3] for y in [4, 5, 6]]

S7 = 'python'
L8 = [x*y for (x, y) in enumerate(S7)]

#
L9 = list(enumerate(open('/home/evgen/pgadmin.log')))

#
F3 = open('/home/evgen/pgadmin.log')
D1 = {key: line for (key, line) in enumerate(F3)}

#
def f(a, b):
    print(a, b, sep='$')

f(1, 2)
f(*[1, 2])

#
L10 = list(zip('abc', 'def'))

#
r = range(0, 10, 2)
L11 = r[2:4]

def square(x):
    return x**2

m = map(square, (1, 2, 3, 4))
z = zip((0, 1, 2), (3, 4, 5))

def test(digit):
    return digit > 0

L12 = filter(test, [1, -20, 5, -4, 0])

def f(d):
    return d % 2

L13 = [1, 2, 3, 4, 5, 6]
filter(f, L13)
