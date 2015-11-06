__author__ = 'evgen'

a = [1, 2, 3, 4, 5]

#
d = {'a': 1, 'b': 1, 'c': 1}
k = sorted(d.keys())
for key in k:
    print(key, ' : ', d[key])

#
squares = [x ** 3 for x in range(0, 11)]

#
cubes = []
for x in range(1, 6):
    cubes.append(x ** 2)
print(cubes)

#
f = {'a': 1, 'b': 2}
if 'c' in f:
    print('c', ' : ', f['c'])
else:
    print('Missing')

#
x = set('spam')
for i in x:
    print(i)

#
a = [1, 2, 3]
b = {'x': 1}
c = (1, 2, 3)

#
type(a) == type([])
type(a) == list
isinstance(a, list)

#
#
#
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1 + percent)


jeka = Worker('Evgen Kasyan', 100000)
vika = Worker('Vika Ryzhyk', 50000)

jeka.last_name()


#
def factorial(digit):
    if digit == 1:
        return 1
    else:
        return factorial(digit - 1)

##
a = 5.2
type(a)

b = 3j + 2

#
a = [2, 3, 2.3, 4, 3.7, 2]

sum = 0
for i in a:
    sum += i
    print('Type of sum: ', type(sum))

#
a = complex(1, 2)
b = 3
c = a + b
type(c)

#
a = 2
b = 3
c = 3//2
type(c)

#
a = 3
b = 4

b/(2.0 + a)

#
x = 2
y = 4
z = 6

x < y < z

#
a = 1.1
b = 1.1
c = a//b
type(c)

x = 100
x.bit_length()

#
from fractions import Fraction
x = Fraction(1, 3)
y = Fraction(2, 4)

#
import decimal
decimal.getcontext().prec = 2
x = decimal.Decimal(1)/decimal.Decimal(3)
y = decimal.Decimal(str(1/3)) + decimal.Decimal(str(2/3))

#
x = (2.5).as_integer_ratio()
print(type(x))

f = 2.5
z = Fraction(*f.as_integer_ratio())

y = float(z)
type(y)

Fraction.from_float(1.75)
Fraction(*(1.75).as_integer_ratio())

#
x = Fraction(*(0.5).as_integer_ratio())

y = x + 2 # = Fraction
y = x + 1/3 # = float
y = x + 2.8 # = float

#
a = Fraction(*(4/3).as_integer_ratio())
a = Fraction(*(4.0/3).as_integer_ratio())

b = a.limit_denominator()