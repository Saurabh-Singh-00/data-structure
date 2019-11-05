try:
    from linked_list.singly_linked_list import SinglyLinkedList
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.singly_linked_list import SinglyLinkedList


class Stack:
    def __init__(self):
        self.__l = SinglyLinkedList()
        self.top = -1

    def push(self, element):
        self.__l.append(element)
        self.top += 1

    def pop(self):
        if self.top == -1:
            raise Exception("Cannot pop from an empty stack")
        self.top -= 1
        return self.__l.pop()

    @property
    def top_item(self):
        if self.top == -1:
            return
        return self.__l.tail

    def __iter__(self):
        for i in self.__l:
            yield i

    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"
