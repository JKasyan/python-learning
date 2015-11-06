__author__ = 'evgen'

first_name, second_name = 'Evgen', 'Kasyan'
print(first_name, ', ', second_name)

a = [first_name, second_name]
a = 'Evgen', 'Kasyan'

a, b, c, d = 'Java'

a, *b = 'Java'


#
first = 1
second = 2
A, B = first, second
a = A, B
type(a)
[C, D] = [first, second]

#
s = 'Java'
a, b, c = s[0], s[1], s[2:]

a, b, c = list(s[:2]) + [s[2:]]

a, b = s[:2]

(a, b), c = s[:2], s[2:]

#
one, two, three = range(3)

#
l = list(range(20))
while l:
    first, l = l[0], l[1:]
    print(first, l)

#
l = [1, 2, 3, 4]
a, b, c, d = l
a, b, *c = l
a, *b = l

*a, b = l

a, *b, c = l
a, b, *c = l

l = list(range(4))
while l:
    first, *l = l
    print(first, " ", l)

#
a, *b, c = 'Java'

# factorial
d = 3
result = 1
while not d == 1:
    result *= d
    d -= 1
print(result)

def factorial(digit):
    r = 1
    while not digit == 1:
        r *= digit
        digit -= 1
    return r

#
l = [1, 2, 3, 4]
a, b, c, *d = l
a, b, c, d, *e = l