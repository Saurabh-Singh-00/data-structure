try:
    from linked_list.singly_linked_list import SinglyLinkedList
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.singly_linked_list import SinglyLinkedList


class Queue:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__l = SinglyLinkedList()
        self.__front = 0
        self.__rear = 0

    @property
    def is_empty(self):
        return self.__front == self.__rear

    @property
    def front(self):
        return self.__front

    @property
    def rear(self):
        return self.__rear

    def enqueue(self, element):
        self.__l.append(element)
        self.__rear += 1

    def dequeue(self):
        self.__front += 1
        if self.is_empty:
            self.__front, self.__rear = 0, 0
        return self.__l.shift()

    def peek(self):
        return self.__l.head

    def __iter__(self):
        for i in self.__l:
            yield i

    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"
