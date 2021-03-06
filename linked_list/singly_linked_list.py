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

    def __init__(self, *args, **kwargs):
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
        return self.head is None and self._length == 0

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
        if self.is_empty:
            raise Exception("Empty List")
        elif len(self) == 1:
            data = self._head
            self._head = None
        else:
            current, previous = self._head, self._head
            while current.next is not None:
                previous = current
                current = current.next
            data = current
            previous.next = None
            self._tail = previous
        self._length -= 1
        if self.is_empty:
            self._tail = None
        return data

    def shift(self, shift_by: int = 1):
        if self.is_empty:
            raise Exception("Cannot perform shift on Empty List")
        elif len(self) < shift_by:
            raise IndexError("Shifting index out of range")
        else:
            temp = None
            while shift_by:
                temp = self._head
                self._head = self._head.next
                self._length -= 1
                shift_by -= 1
            if len(self) == 0:
                self._tail = None
            temp.next = None
            return temp

    def unshift(self, element):
        if self.is_empty:
            self.append(element)
        else:
            temp = self.__Node(element)
            temp.next = self._head
            self._head = temp
            self._length += 1

    def remove(self, element):
        if self.is_empty:
            raise ValueError(
                "Element %s does not exists in the list" % str(element))
        else:
            temp_index, previous, current = 0, self._head, self._head
            while temp_index < len(self):
                if current.data == element:
                    break
                previous = current
                current = current.next
                temp_index += 1
            if temp_index == 0:
                self.shift()
            elif temp_index == len(self) - 1:
                self.pop()
            elif temp_index == len(self):
                raise ValueError(
                    "Element %s does not exists in the list" % element)
            else:
                previous.next = current.next
                current.next = None
                self._length -= 1

    def reverse(self):
        if len(self) == 0 or len(self) == 1:
            return self
        else:
            node = self._head
            self._head, self._tail = self._tail, self._head
            next_node, previous_node = None, None
            for i in range(len(self)):
                next_node = node.next
                node.next = previous_node
                previous_node = node
                node = next_node
            return self

    def __len__(self):
        return self._length

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def _bounded_index(self, index):
        if index < 0:
            index = self._length + index
        if index > self._length - 1 or index < 0:
            raise IndexError("List index out of range")
        return index

    def __getitem__(self, index):
        index = self._bounded_index(index)
        temp_index, temp = 0, self._head
        while temp_index != index:
            temp = temp.next
            temp_index += 1
        return temp

    def __setitem__(self, index, element):
        if self.is_empty:
            raise IndexError("List index out of range")
        index = self._bounded_index(index)
        temp_index, current = 0, self._head
        while temp_index != index:
            current = current.next
            temp_index += 1
        current.data = element

    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"
