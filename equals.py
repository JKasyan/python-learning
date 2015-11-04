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