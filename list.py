__author__ = 'Evgen'

list_1 = [1, 2, 3]
list_2 = [3, 5, 6]

list_3 = list_1 + list_2

a = list(map(abs, [-2, -1, 0, 1, 2]))

#
L = [1, 2, 3, 4, 5, 6]
L[0:2] = [10, 30, 40, 50]
L[0:2] = []

#
A = [2, 3]
A.append(1)
A[len(A):] = [7]
A[:0] = [4]

#
D = ['abc', 'ABD', 'aBe']
D.sort()

D = ['abc', 'ABD', 'aBe']
D.sort(key=str.lower)

D = ['abc', 'ABD', 'aBe']
D.sort(key=str.lower, reverse=True)

#
L = [1, 5, 8, 4, 66, 3]
L1 = sorted(L, reverse=1)

#
L = [1, 2, 3, 4]
del L[0]

L.extend([1, 2, 3])
L.pop()