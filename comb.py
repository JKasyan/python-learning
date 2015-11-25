__author__ = 'Evgen'

def factorial(d):
    result = 1
    while d:
        result *= d
        d -= 1
    return result

def bubble_sort(seq):
    length = len(seq) - 1
    while length:
        for i in range(length):
            if seq[i] > seq[i+1]:
                tmp = seq[i]
                seq[i] = seq[i+1]
                seq[i+1] = tmp
        length -= 1

L = [1, 5, 37, 8]

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
    print()

f1 = lambda x: (x+2)/2
f2 = lambda x: x**2

functions = [f1, f2, lambda x: x**x]

for f in functions:
    print(f(7))

def f3(n):
    c = n
    f4 = lambda x: c**x
    return f4

def f5(a, b):
    return a + b

def intersect(seq_one, seq_two):
    if seq_one == seq_two:
        return seq_one
    result = []
    for i in seq_one:
        if i in seq_two:
            result.append(i)
    return result

def intersect(seq_one, seq_two):
    return [x for x in seq_one if x in seq_two]

def is_odd(d):
    """
    Check the length of
    sequence is odd
    """
    return len(d) & 0x01
