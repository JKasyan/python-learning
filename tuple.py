__author__ = 'Evgen'

t1 = 1, 2, 3
t2 = 4, 5, 6

t = t1 + t2
print(t)

d = (4)
t = (4,)
type(d)
type(t)

#
t = 1, 5, 7, 8, 9, 4, 6, 3
l = list(t)
l.sort()
t = tuple(l)

t = 1, 5, 7, 8, 9, 4, 6, 3
t = sorted(t)

#
t = 1, 2, 3, 4, 5, 6, 7
t.index(2)
t.count(2)