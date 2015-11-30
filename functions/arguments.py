__author__ = 'evgen'

L = [1, 2, 3]

def change_one(L):
    for i in range(len(L)):
        L[i] = 100

change_one(L[:])
change_one(tuple(L))
print(L)

def change_two(L):
    L = L[:]

"""
"""

def multiple(x, y):
    x = 5
    y = [1, 2]
    return x, y

t = multiple(6, 7)