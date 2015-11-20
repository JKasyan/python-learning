__author__ = 'evgen'

file = open('/home/evgen/pgadmin.log')
for line in file:
    print(line, end='')

for line in open('/home/evgen/pgadmin.log').readlines():
    print(line, end='')

while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')

#
L = [1, 2, 3]
I = iter(L)
el = I.__next__


#
L1 = [1, 2, 3, 4]
for L in L1:
    print(L**2)

iterator = iter(L1)
while True:
    try:
        el = next(iterator)
    except StopIteration:
        break
    print(el)

D1 = {'a': 1, 'b': 2}
for key in D1.keys():
    print(key, '===', D1[key])

for key in D1:
    print(key)

def print_dict(dictionary):
    i = iter(dictionary)
    while True:
        try:
            key = next(i)
        except StopIteration:
            break
        print(key, ' : ', dictionary[key])
