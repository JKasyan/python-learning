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

    # def __bool__(self):
    #     return len(self.array) != 0

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        return self.array[item]


m = re.match('[a-zA-Z0-1]{3,10}?@[a-z]{3,10}.(com|net)', 'sdsd@gmail.com')
print(m)


stack = Stack()
stack.add(1)
print('__getitem__ = ', stack[0])
print(bool(stack))