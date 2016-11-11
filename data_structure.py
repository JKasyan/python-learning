
class LinkedList:
    def __init__(self):
        self.tail = LinkedList.Entry(None, None, None)
        self.size = 0

    def pop(self):
        if self.size == 0:
            return None
        last = self.tail.prev
        last.prev.next_el = self.tail
        self.tail.prev = last.prev
        last.next_el = None
        last.prev = None
        self.size -= 1
        return last.value

    def add(self, el):
        # first element
        if self.size == 0:
            entry = LinkedList.Entry(self.tail, el, self.tail)
            self.tail.next_el = entry
            self.tail.prev = entry
        else:
            last = self.tail.prev
            entry = LinkedList.Entry(last, el, self.tail)
            last.next_el = entry
            self.tail.prev = entry
        self.size += 1

    def get(self, index):
        if 0 < index > self.size - 1:
            raise ArithmeticError('index must be more 0 and less ' + str(self.size))
        if index < self.size / 2:
            ref = self.tail.next_el
            for number in range(0, index):
                ref = ref.next_el
            return ref.value
        else:
            ref = self.tail.prev
            for number in range(0, self.size - index - 1):
                ref = ref.prev
            return ref.value

    """
        Remove by index
    """
    def remove(self, index):
        if 0 < index > self.size - 1:
            raise ArithmeticError('index must be more 0 and less ' + str(self.size))
        if index < self.size / 2:
            ref = self.tail.next_el
            for number in range(0, index):
                ref = ref.next_el
            ref.prev.next_el = ref.next_el
            ref.next_el.prev = ref.prev
            ref.prev = None
            ref.next_el = None
            return ref.value
        else:
            ref = self.tail.prev
            for number in range(0, self.size - index - 1):
                ref = ref.prev
            ref.prev.next_el = ref.next_el
            ref.next_el.prev = ref.prev
            ref.prev = None
            ref.next_el = None
            return ref.value

    def to_list(self):
        l = []
        if self.tail.next_el is None:
            return l
        ref = self.tail.next_el
        while ref != self.tail:
            l.append(ref.value)
            ref = ref.next_el
        return l

    def __str__(self):
        text = 'LinkedList[ '
        ref = self.tail.next_el
        for number in range(0, self.size):
            text += str(ref.value) + ', '
            ref = ref.next_el
        return text[:-2] + ']'

    class Entry:
        def __init__(self, prev, value, next_el):
            self.next_el = next_el
            self.value = value
            self.prev = prev

        def __str__(self):
            return str(self.value)

    def is_empty(self):
        return self.size == 0


link_list = LinkedList()
for i in 'python':
    link_list.add(i)
link_list.add({'a': 1, 'b': 2})
print(link_list.remove(1))
print(link_list)
print(link_list.get(link_list.size - 1))
print(link_list.to_list())
# print(link_list.pop())
print(link_list.tail is None)
