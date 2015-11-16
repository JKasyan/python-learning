__author__ = 'Evgen'

print(1, 2, 3, 4, sep=';', end='\n')

print(1, 2, 3, sep=';', end='...\n')

print(1, 2, 3, sep='\n', file=open('C:\\Users\\Evgen\\Desktop\\data.txt', 'w'))

print(open('data.txt').read())

#
text = "%s: %-.4f, %05d" % ('Result', 3.14159, 42)
print(text)

#
import sys
temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print('spam')
print(1, 2, 3)
sys.stdout.close()
sys.stdout = temp
print('Back here')
print(open('log.txt').read())

#
log = open('log.txt', 'a')
print(1, 2, 3, file=log)
print(1, 2, 3)