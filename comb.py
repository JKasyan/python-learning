__author__ = 'Evgen'

def factorial(d):
    result = 1
    while d:
        result *= d
        d -= 1
    return result