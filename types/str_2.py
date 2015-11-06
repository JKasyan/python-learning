__author__ = 'Evgen'

a = 'Jeka is %s' % 'man'

t = (1, 'notebook')
a = 'I have %i %s' % t
print(a)

a = '%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0)


#
a = '%(n)d %(x)s' % {'n': 1, 'x': 'spam'}
print(a)

#
reply = '''
Greetings...
Hello %(name)s
Your age squared is %(age)s
'''
values = {'name': 'Bob', 'age': 40}
print(reply % values)

#
template = '{0}, {1} and {2}'
template = template.format('spam', 'ham', 'eggs')

#
import sys
a = 'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'platform'})

l = list('spam')
c = 'first = {0[0]}, second = {0[1]}'.format(l)


#
a = '{0:10} = {1:10}'.format('spam', 123.456)
a = '{0:>10} = {1:<10}'.format('spam', 123.456)
import sys
a = '{0.platform:>10} = {1[item]:<10}'.format(sys, {'item': 'laptop'})

#
#
c = '{0:.3f}'.format(1.2345)
c = '%.2f' % 1.2345
c = format(1.2345, '.2f')
c = '%.*f' % (4, 1.234567)

#
print('%s = %s' % ('spam', 42))
a = '%b' % (2**16)
a = 'My {} is {}'.format('name', 'bob')
a = 'My %s is %s' % ('name', 'Bob')

b = '{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159)
c = '{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159)
d = '%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159)

a = (1, 2, 3)
b = 'first = %i, second = %i, third = %i' % a