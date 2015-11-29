__author__ = 'evgen'

x = 99

def f1():
    x = 88
    def f2():
        print(x)
    f2()

f1()

###

def f3():
    x = 88
    def f4():
        print(x)
    return f4

action = f3()
action()


"""
Closure
"""

def maker(N):
    def action(X):
        return X ** N
    return action

f5 = maker(2)
f6 = maker(3)

def power(N):
    return lambda X: N ** X

"""
Default parameter
"""

def f7(x = 100):
    print(x)

f7()
f7(200)

"""
Without enclosing
"""

def f8():
    x = 100
    def f9(x=x):
        print(x)
    f9()

"""
Equal previous function
"""

def f10():
    x = 88
    f11(x)

def f11(x):
    print(x)

f10()

"""
Inner lambda without enclosing
"""

def f12(x):
    return lambda n, x = x: x ** n

"""
Cycle and inner function
"""

def makeFunctions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts

for f in makeFunctions():
    print(f(2))

"""
Decision
"""

def functions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i = i: x ** i)
    return acts

for f in functions():
    print(f(2))

"""
Enclosing
"""

def f13():
    x = 99
    def f14():
        def f15():
            print(x)
        f15()
    f14()
f13()

"""
Non local
"""

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')
F('ham')

