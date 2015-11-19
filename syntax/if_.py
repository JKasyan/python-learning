__author__ = 'Evgen'

if 1:
    print('true')

#
a = 5
if a == 10:
    print("Ten")
elif a == 20:
    print('20')
elif a == 5:
    print('Five')
else:
    print("Undefined")

#
choice = 'ham'
dictionary = {'ham': 20, 'spam': 30}
print(dictionary.get(choice, 'Undefined'))

#
choice = 4
dictionary = {1: 'One', 2: 'Two', 3: 'Three'}
if choice in dictionary:
    print(dictionary[choice])
else:
    print('Bad choice')

#
x = 1
if x:
    y = 2
    if y:
        print('block 2')
    print('block 1')
print('block 0')

#
x = 'spam'
if 'rubbery' in 'shrubbery':
    print(x*8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)


#
a = [1,
     2,
     3,
     4]

b = (1,
     2,
     3,
     4)

c = {
    'a': 1,
    'b': 2,
    'c': 3
}

#
a = \
20
b = 20

if a > 0 and \
    b < 30:
    print("Hello")

if (a > 0 and
b < 30):
    print('Hello')

#
S = (
    'aaaa'
    'bbbb'
    'cccc'
)
print(S)

if 1: print('python')

a = [1, 2, 3]
b = (1, 2)
result = a > b