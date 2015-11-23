__author__ = 'evgen'

import builtins

dir(builtins)

def f1():
    def open(filePath):
        print('Local open: ', filePath)
    open("filePath")

"""
Global variable
"""
X, Y, Z = 99, 100, 101

def f2():
    global X, Y, Z
    X, Y, Z = 20, 30, 40
f2()
print(X, Y, Z, sep=";")

###
def f3():
    global not_existing_global_var
    not_existing_global_var = 20
f3()
print(not_existing_global_var)

###
y, z = [20, 30]
def f4():
    global var
    var = y + z

f4()
print(var)