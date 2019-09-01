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
            previous = self._tail.previous
            previous.next = None
            self._tail = previous
        self._length -= 1
        return data

    def shift(self, shift_by=1):
        pass

    def unshift(self, element):
        pass

    def remove(self, element):
        pass

    def reverse(self):
        pass


if __name__ == "__main__":
    l = DoublyLinkedList()
    for i in range(10):
        l.append(i)
    for i in l:
        print(i)
    l[-1] = 90
    print(l.head, l.tail, len(l))
