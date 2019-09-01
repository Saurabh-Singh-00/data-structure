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
        tail = self._tail
        super().append(element)
        self._tail.previous = tail

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
        super().shift(shift_by=shift_by)
        if not self.is_empty:
            self._head.previous = None

    def unshift(self, element):        
        super().unshift(element)
        if len(self) > 1:
            self._head.next.previous = self._head
        

    def remove(self, element):
        pass # TODO: Implement remove

    def reverse(self):
        pass # TODO: Implement reverse


if __name__ == "__main__":
    l = DoublyLinkedList()
    for i in range(10):
        l.append(i)
    for i in l:
        print(i)
    l.shift(10)
    l.unshift(100)
    print(l.head, l.tail)
    l[-1] = 90
    print(l.head, l.tail, len(l))
    print(l)
