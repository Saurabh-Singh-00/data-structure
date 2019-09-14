try:
    from .abstract_node import AbstractNode
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.abstract_node import AbstractNode
    from linked_list.singly_linked_list import SinglyLinkedList


class DoublyLinkedList(SinglyLinkedList):

    class __Node(AbstractNode):
        def __init__(self, data):
            super().__init__(data)
            self.next = None
            self.previous = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append(self, element):
        node = self.__Node(element)
        if self.is_empty:
            self._head = node
            self._tail = self._head
        else:
            node.previous = self._tail
            self._tail.next = node
            self._tail = self.tail.next
        self._length += 1

    def pop(self):
        data = self._tail
        if self.is_empty:
            raise Exception("Empty List")
            return
        elif len(self) == 1:
            self._tail = None
            self._head = None
        else:
            self._tail = data.previous
            self._tail.next = None
            data.previous = None
        self._length -= 1
        return data

    def shift(self, shift_by=1):
        if self.is_empty:
            raise Exception("Cannot perform shift on Empty List")
        elif len(self) < shift_by:
            raise IndexError("Shifting index out of range")
        else:
            while shift_by:
                temp = self._head
                self._head = temp.next
                self._head.previous = None
                temp.next = None
                self._length -= 1
                shift_by -= 1
            if len(self) == 0:
                self._head = None
                self._tail = None
            return temp

    def unshift(self, element):
        node = self.__Node(element)
        if self.is_empty:
            self.append(element)
        else:
            self._head.previous = node
            node.next = self._head
            self._head = self._head.previous
            self._length += 1

    def remove(self, element):
        if self.is_empty:
            raise Exception("Empty List")
        else:
            temp, index = self._head, 0
            while index < len(self):
                if temp.data == element:
                    break
                index += 1
                temp = temp.next
            if index == 0:
                self.shift()
            elif index == len(self) - 1:
                self.pop()
            elif index == len(self):
                raise ValueError(
                    "Element %s does not exists in the list" % element)
            else:
                temp.previous.next = temp.next
                temp.next, temp.previous = None, None
                self._length -= 1

    def insert(self, index, value):
        index = self._bounded_index(index)
        if index == 0:
            self.unshift(value)
        else:
            temp_index, temp = 0, self._head
            while temp_index < index-1:
                temp = temp.next
                temp_index += 1
            save_next = temp.next
            temp.next = self.__Node(value)
            temp.next.previous = temp
            temp.next.next = save_next
            save_next.previous = temp.next
            self._length += 1

    def reverse(self):
        if self.is_empty or len(self) == 1:
            return self
        index, current = 0, self._head
        while index < len(self):
            temp, next_node = current, current.next
            current.next = current.previous
            current.previous = next_node
            current = current.previous
            index += 1
        self._head, self._tail = self._tail, self._head
        return self
