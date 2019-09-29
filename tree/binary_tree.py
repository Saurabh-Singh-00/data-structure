class BinaryTree:

    class Node:

        def __init__(self, data):
            self.data = data
            self.l_child = None
            self.r_child = None

        @property
        def is_leaf(self):
            return self.l_child is None and self.r_child is None

        @property
        def has_one_child(self):
            return (self.l_child is not None and self.r_child is None) or (self.l_child is None and self.r_child is not None)

        @property
        def is_intermediate(self):
            return self.l_child != None and self.r_child != None

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None
        self._height = 0

    def height(self, root):
        if root is None:
            return -1
        return max(self.height(root.l_child), self.height(root.r_child))+1

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            current = self.root
            _root = current
            while current:
                _root = current
                if data < current.data:
                    current = current.l_child
                else:
                    current = current.r_child
            if data < _root.data:
                _root.l_child = self.Node(data)
            else:
                _root.r_child = self.Node(data)

    def search(self, value):
        if self.root is None:
            raise Exception("Value {} does not exists".format(value))
        current = self.root
        parent = current
        while current is not None and value != current.data:
            parent = current
            if value < current.data:
                current = current.l_child
            else:
                current = current.r_child
        if current is None:
            raise Exception("Value {} does not exists".format(value))
        return current, parent

    def __min_value_node(self, node: Node) -> Node:
        if node.l_child is None:
            return node
        return self.__min_value_node(node.l_child)

    def delete(self, value):
        current, parent = self.search(value)
        if current.is_leaf:
            if current is parent.l_child:
                parent.l_child = None
            elif current is parent.r_child:
                parent.r_child = None
            else:
                self.root = None
        elif current.has_one_child:
            if current is parent.l_child:
                parent.l_child = current.l_child if current.l_child is not None else current.r_child
            elif current is parent.r_child:
                parent.r_child = current.l_child if current.l_child is not None else current.r_child
            elif current is parent:
                self.root = current.l_child if current.l_child is not None else current.r_child
        elif current.is_intermediate:
            min_node, min_parent = self.search(
                self.__min_value_node(current.r_child).data)
            current.data = min_node.data
            if min_node is min_parent.l_child:
                min_parent.l_child = None if min_node.is_leaf else min_node.r_child
            elif min_node is min_parent.r_child:
                min_parent.r_child = min_node.r_child
            del min_node
