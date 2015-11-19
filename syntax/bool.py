__author__ = 'evgen'

if 0 or 2:
    print('True')

a = 5
b = a > 2
type(b)

c = 2 or 3, 3 or 2
d = [] or 3

#
a = 5
z = 'first' if a > 0 else 'second'
e = ((a > 0 and 'first') or 'second')
y = ['second', 'first'][bool('')]

k = 1
l = 2
n = 3
s = k or l or n or None

def f1():
    print('f1()')
    return None

def f2():
    print('f2()')
    return 1

m = f2() or f1()
