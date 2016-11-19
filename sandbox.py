import re
import data_structure


class Stack:
    def __init__(self):
        self.array = []

    def add(self, el):
        self.array.append(el)

    def pop(self):
        return self.array.pop(len(self.array) - 1)

    def __str__(self):
        return 'Stack: ' + str(self.array)


m = re.match('[a-zA-Z0-1]{3,10}?@[a-z]{3,10}.(com|net)', 'sdsd@gmail.com')
print(m)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return self.name.__hash__() + self.age.__hash__()

    def __str__(self):
        return 'Person{ name = ' + self.name + ', age = ' + str(self.age) + ' }'

p1 = Person('John', 30)
p2 = Person('John', 30)
print(p1)
d = {}
d[('John', 30)] = 1
print(('John', 30) in d)

l = data_structure.LinkedList()
print(l)