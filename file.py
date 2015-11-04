__author__ = 'Evgen'

f = open('C:\\Users\\Evgen\\Desktop\\test.txt', 'w')
f.write('Hello')
lines = ['Hello\n', 'world\n', '\t']
f.writelines(lines)
f.readable()
f.flush()

f = open('C:\\Users\\Evgen\\Desktop\\test.txt', 'r')
f.readlines()

#
for line in open('C:\\Users\\Evgen\\Desktop\\test.txt', 'r'):
    print(line, end='')
