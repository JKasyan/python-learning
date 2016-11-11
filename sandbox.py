import re


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


