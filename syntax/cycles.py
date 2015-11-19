
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

#
(a, *b, c) = 1, 2, 3, 4
for (a, *b, c) in ((1, 2, 3, 4), (5, 6, 7, 8)):
    print(a, b, c)

for A in [[1, 2, 3, 4], [5, 6, 7, 8]]:
    a, b, c = A[0], A[1:3], A[3]
    print(a, b, c)

t = (1, 2, 3, 4)
l = [1, 2, 3, 4]

t = t[1:2]
l = l[1:2]

for (a, *b, c) in ([1, 2, 3], [4, 5, 6]):
    print(a, b, c)

#
items = ['asd', (1, 2), [3, 4], {'a': 20}]
tests = (1, 'dfg', [3, 4])

for key in tests:
    for item in items:
        if item == key:
            print(key, ' was found')
            break
    else:
        print(key, ' not found')

for key in tests:
    if key in items:
        print(key, ' was found')
    else:
        print(key, ' not found')

#
seq1 = 'spam'
seq2 = 'scan'
res = []
for c in seq1:
    if c in seq2:
        res.append(c)
print(res)

#
file = open('test.txt')
while True:
    char = file.read(1)
    if not char:
        break
    print(char)

for char in file.read():
    print(char)

#
l1 = list(range(5))
l2 = list(range(2, 5))
l3 = list(range(0, 10, 2))

#
x = 'python'
for c in x:
    print(c)

i = 0
l = len(x)
while i < l:
    print(x[i])
    i += 1

for c in range(len(x)):
    print(x[c])

#
x = 'abcdefghijk'

for i in range(0, len(x), 3):
    print(x[i])

for c in x[::2]:
    print(c)

#
L = [7, 8, 9, 10, 11]
for i in range(len(L)):
    L[i] += 1

i = 0
l = len(L)
while l:
    L[i] += 1
    i += 1
    l -= 1

L = [x+1 for x in L]

#
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

L3 = list(zip(L1, L2))

for (a, b) in zip(L1, L2):
    print(a + b, "---", a**b)

i = 0
l = len(L1)
while i < l:
    print(L1[i] + L2[i], '---', L1[i]**L2[i])
    i += 1

L4 = [9, 10]
for (a, b, c) in zip(L1, L2, L4):
    print(a, b, c, '---', a + b + c)

L5 = [1, 2, 3]
S1 = 'abc'
T1 = (4, 5, 6)
L = list(zip(L5, S1, T1))