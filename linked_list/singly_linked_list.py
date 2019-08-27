try:
    from .abstract_node import AbstractNode
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.abstract_node import AbstractNode


class SinglyLinkedList:

    class __Node(AbstractNode):
        def __init__(self, data):
            super(self.__class__, self).__init__(data)
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def is_empty(self):
        return self.head is None

    def append(self, data):
        node = self.__Node(data)
        if self.is_empty:
            self._head = node
            self._tail = self._head
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._length += 1

    def pop(self):
        data = None
        if self.is_empty is None:
            raise Exception("Empty List")
        elif len(self) == 1:
            data = self._head
            self._head = None
            self._tail = None
        else:
            current, previous = self._head.next, self._head
            while current.next is not None:
                previous = current
                current = current.next
            data = current
            previous.next = None
            self._tail = previous
        self._length -= 1
        return data

    def shift(self, shift_by: int = 1):
        if self.is_empty:
            raise Exception("Cannot perform shift on Empty List")
        elif len(self) < shift_by:
            raise IndexError("Shifting index out of range")
        else:
            while shift_by:
                self._head = self._head.next
                self._length -= 1
                shift_by -= 1
            if len(self) == 0:
                self._tail = None

    def unshift(self, element):
        if self.is_empty:
            self.append(element)
        else:
            temp = self.__Node(element)
            temp.next = self._head
            self._head = temp
            self._length += 1

    def __len__(self):
        return self._length

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __getitem__(self, index):
        if index > self._length - 1:
            raise IndexError("List index out of range")
        else:
            _index, temp = 0, self._head
            while _index != index:
                temp = temp.next
                _index += 1
            return temp

    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"


if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(1, 11):
        l.append(i*10)
    l.shift(shift_by=9)
    l.shift()
    print(l)
    print(l.head, l.tail)
    l.unshift(10)
    print(l[0])
    l.unshift(20)
    l.pop()
    print(l)
