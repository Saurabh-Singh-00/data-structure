class SinglyLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next_node = None

        def __str__(self):
            return "{}".format(self.data)

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        if self.head is None:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.tail.next_node = self.Node(data)
            self.tail = self.tail.next_node
        self.length += 1

    def search(self, data):
        _ = self.head
        index = -1
        if self.length == 0:
            return index
        while _ is not None:
            if data == _.data:
                return index + 1
            _ = _.next_node
            index += 1
        return -1

    def remove(self, data: int):
        index = self.search(data)
        if index == -1:
            raise Exception(
                "Value {} doesn\'t exists in the list".format(data))
        else:
            _ = self.head
            previous = _
            find = 0
            while find <= index:
                if find == index:
                    break
                previous = _
                _ = _.next_node
                find += 1
            next_node = None
            self.length -= 1
            if previous is self.head:
                self.head = self.head.next_node
            if _.next_node is not None:
                next_node = _.next_node
                previous.next_node = next_node
            else:
                previous.next_node = None

    def insert(self, index: int, data):
        if self.length == 0:
            raise Exception(
                "Cannot insert into empty list use list.append() instead")
        if -1 < index < self.length-1:
            _ = self.Node(data)
            if index == 0:
                _.next_node = self.head
                self.head = _
            else:
                traverse = 0
                current = self.head
                previous = current
                while traverse <= index:
                    if index == traverse:
                        break
                    previous = current
                    current = current.next_node
                # TODO:: Complete insert function
            self.length += 1
        else:
            raise IndexError("Index out of range")

    def pop(self):
        if self.head is None:
            raise IndexError("Cannot pop from an Empty List")
        _ = self.head
        data = None
        previous = _
        while _.next_node is not None:
            previous = _
            _ = _.next_node
        data = _.data
        if previous is _:
            self.head = None
        else:
            previous.next_node = None
        self.length -= 1
        return data

    def __iter__(self):
        _ = self.head
        while _ is not None:
            yield _.data
            _ = _.next_node

    def __len__(self):
        return self.length

    def __str__(self):
        return "[" + ", ".join([str(_) for _ in self]) + "]"


l = SinglyLinkedList()
l.append(0)
l.append(10)
l.append(1)
l.pop()
l.remove(0)
