class LinkedList:
    def __init__(self):
        self.tail = LinkedList.Entry(None, None, None)
        self.size = 0

    def __len__(self):
        return self.size

    def pop(self):
        if self.size == 0:
            return None
        last = self.tail.prev
        last.prev.next_el = last.next_el
        self.tail.prev = last.prev
        last.next_el = None
        last.prev = None
        self.size -= 1
        return last.value

    def __contains__(self, item):
        ref = self.tail.next_el
        for i in range(0, self.size):
            if ref.value == item:
                return True
            ref = ref.next_el
        return False

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

    def add_by_index(self, el, index):
        if 0 < index > self.size - 1:
            raise ArithmeticError('index must be more 0 and less ' + str(self.size))
        ref = self.tail.next_el
        if index < self.size / 2:
            for number in range(0, index):
                ref = ref.next_el
        else:
            for number in range(0, self.size - index - 1):
                ref = ref.prev
        entry = LinkedList.Entry(ref, el, ref.next_el)
        ref.next_el.prev = entry
        ref.next_el = entry
        self.size += 1

    def __getitem__(self, index):
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
    def __delitem__(self, index):
        if 0 < index > self.size - 1:
            raise ArithmeticError('index must be more 0 and less ' + str(self.size))
        ref = self.tail.next_el
        if index < self.size / 2:
            for number in range(0, index):
                ref = ref.next_el
        else:
            for number in range(0, self.size - index - 1):
                ref = ref.prev
        ref.prev.next_el = ref.next_el
        ref.next_el.prev = ref.prev
        ref.prev = None
        ref.next_el = None
        self.size -= 1
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
        if self.size == 0:
            return text + ']'
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
link_list.add(1)
link_list.add(2)
link_list.add(4)
link_list.add_by_index(3, 1)
del link_list[0]
print('Linked list = ', link_list)
print('__len__ ', len(link_list))
print('__contains__ ', 2 in link_list, 'Python' in link_list)
#
#
#
