__author__ = 'evgen'

file_address = 'c:\new\text'
print(file_address)
file_address = r'c:\new\text'
print(file_address)

#
a = '''My
name
is
John'''
print(a)

#
hello = '-'*10 + 'Hello' + '-'*10

#
s = 'spam'
m = s[-1]

#
s = 'abcdefghijklmnop'
c = s[1:10:2]

name = 'Jeka'
name = name[::-1]

#
ord('s')
chr(115)

d = '1101'
digit = 0
while d != '':
    digit = digit*2 + (ord(d[0]) - ord('0'))
    d = d[1:]
print(digit)

#
a = 'That is %d %s bird!' % (1, 'dead')
b = 'That is {0} {1} bird!'.format(1, 'dead')

#
s = '5'
s.isdigit()