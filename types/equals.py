__author__ = 'Evgen'

result = 1
s1 = ''
s2 = ''
while result == 1:
    s1 += "a"
    s2 += "a"
    print(s1)
    result = s1 is s2
print(len(s2))

#
a = {}
if a:
    print('Not empty')
else:
    print("Empty")

a = True
if a:
    print(True)

a = [1, 2, 3]
b = [2, 3, 4]

print(type(a) is type(b))

L = [4, 5, 6]
X = L*4
Y = [L] * 4

#
L = [1, 2, 3]
L.append(L)