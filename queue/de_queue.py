try:
    from linked_list.singly_linked_list import SinglyLinkedList
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.singly_linked_list import SinglyLinkedList


class DEQueue:
    ''' Double Ended Queue '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__l = SinglyLinkedList()
        self.__front = -1
        self.__rear = -1

    @property
    def is_empty(self):
        return self.__front == self.__rear

    @property
    def front(self):
        return self.__front

    @property
    def rear(self):
        return self.__rear

    def f_enqueue(self, element):
        ''' Enqueue from front '''
        if self.__front == -1:
            raise Exception("Cannot insert from front try r_enqueue() instead")
        else:
            self.__l.unshift(element)
            self.__front -= 1

    def r_enqueue(self, element):
        ''' Enqueue from rear '''
        self.__l.append(element)
        self.__rear += 1

    def f_dequeue(self):
        ''' Dequeue from front '''
        if self.is_empty:
            return None
        self.__front += 1
        if self.is_empty:
            self.__front, self.__rear = -1, -1
        return self.__l.shift()

    def r_dequeue(self):
        ''' Dequeue from rear '''
        if self.is_empty:
            return None
        self.__rear -= 1
        if self.is_empty:
            self.__front, self.__rear = -1, -1
        return self.__l.pop()

    def __iter__(self):
        for i in self.__l:
            yield i

    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"
