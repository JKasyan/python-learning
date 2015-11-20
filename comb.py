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