try:
    from linked_list.singly_linked_list import SinglyLinkedList
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.singly_linked_list import SinglyLinkedList


class MaxBinaryHeap:

    def __init__(self):
        self.values = SinglyLinkedList()

    def swap(self, node_1, node_2):
        node_1.data, node_2.data = node_2.data, node_1.data

    def __bubble_up(self):
        if len(self.values) == 1:
            return
        index = len(self.values) - 1
        parent = (index - 1) // 2
        while (self.values[index].data > self.values[parent].data) and index > 0:
            self.swap(self.values[index], self.values[parent])
            index = parent
            parent = (index - 1) // 2

    def insert(self, values):
        for value in values:
            self.values.append(value)
            self.__bubble_up()

    def __sink_down(self):
        if len(self.values) == 1:
            return
        index = 0
        l_child, r_child = 2*index + 1, 2*index + 2
        if len(self.values) == 2:
            if self.values[index].data > self.values[l_child].data:
                self.swap(self.values[index], self.values[l_child])

        while (r_child < len(self.values) and l_child < len(self.values)) and ((self.values[index].data < self.values[l_child].data) or
                                                                               (self.values[index].data < self.values[r_child].data)):
            if self.values[l_child].data > self.values[r_child].data:
                self.swap(self.values[index], self.values[l_child])
                index = l_child
            else:
                self.swap(self.values[index], self.values[r_child])
                index = r_child
            l_child, r_child = 2*index + 1, 2*index + 2

    def extract_max(self):
        if self.values.is_empty:
            return
        max_element = self.values.head.data
        self.values.head.data = self.values.tail.data
        self.values.pop()
        self.__sink_down()
        return max_element

    def __str__(self):
        return str(self.values)


class PriorityQueue:
    """\n
    >>> p_queue = PriorityQueue()
    >>> p_queue.enqueue([("Flu", 24), ("Attack", 88), ("Fever", 56), ("Headache", 14)])
    >>> print(p_queue)
    >>> [{Data: Attack, Priority: 88}, {Data: Flu, Priority: 24}, {Data: Fever, Priority: 56}, {Data: Headache, Priority: 14}]

    Using a Hospital Metaphor: Suppose there are multiple cases in a Hospital 
    and they want to operate the case with highest priority/serverity then 
    priority queue can be used as illustrated above.\n
    """
    class Node:
        def __init__(self, data, priority):
            self.data = data
            self.priority = priority

        def __gt__(self, value):
            return self.priority > value.priority

        def __lt__(self, value):
            return self.priority < value.priority

        def __eq__(self, value):
            return self.priority == value.priority

        def __str__(self):
            return "{{Data: {}, Priority: {}}}".format(self.data, self.priority)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__heap = MaxBinaryHeap()

    def enqueue(self, values: list):
        self.__heap.insert(list(map(lambda n: self.Node(n[0], n[1]), values)))

    def dequeue(self):
        return self.__heap.extract_max()

    def __str__(self):
        return str(self.__heap)


p_queue = PriorityQueue()
p_queue.enqueue([("Flu", 24), ("Attack", 88), ("Fever", 56), ("Headache", 14)])
print(p_queue)
print(p_queue.dequeue())
print(p_queue)
