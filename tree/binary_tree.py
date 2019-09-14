class BinaryTree:

    IN_ORDER, PRE_ORDER, POST_ORDER = 0, 1, 2

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
            return self.l_child is not None or self.r_child is not None

        @property
        def is_intermediate(self):
            return self.l_child is not None and self.r_child is not None

        def __str__(self):            
            if BinaryTree.PRE_ORDER:
                return "{{\nNode: {{\n\tdata: {}, \n\tleft: {}, \n\tright: {}\n}}\n}}".format( self.data, self.l_child, self.r_child)
            elif BinaryTree.IN_ORDER:
                return "{{\nNode:{{\n\tleft: {},\n\tdata: {},\n\tright: {}\n}}\n}}".format( self.l_child, self.data, self.r_child)
            elif BinaryTree.POST_ORDER:
                return "{{Node: {{left: {}, right: {}, data: {} }}}}".format( self.l_child, self.r_child, self.data)

    def __init__(self):
        self.root = None
        self._height = 0

    @property
    def height(self):
        return self._height

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

    def traverse(self, mode):
        if mode == BinaryTree.IN_ORDER:
            print("In Order traversal: Left->Data->Right")
            BinaryTree.IN_ORDER, BinaryTree.PRE_ORDER, BinaryTree.POST_ORDER = True, False, False
        elif mode == BinaryTree.PRE_ORDER:
            print("Pre Order traversal: Data->Left->Right")
            BinaryTree.IN_ORDER, BinaryTree.PRE_ORDER, BinaryTree.POST_ORDER = False, True, False
        elif mode == BinaryTree.POST_ORDER:
            print("Post Order traversal: Left->Right->Data")
            BinaryTree.IN_ORDER, BinaryTree.PRE_ORDER, BinaryTree.POST_ORDER = False, False, True
        print(self.root)

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

    def delete(self, value):
        try:
            current, parent = self.search(value)
            # case 1: Delete leaf node
            if current.is_leaf:
                if current is parent.l_child:
                    parent.l_child = None
                else:
                    parent.r_child = None
                del current
            # case 2: Delete a node with one child
            elif current.has_one_child:
                pass
            # case 3: Delete a node with two children
            elif current.is_intermediate:
                pass
        except Exception as e:
            raise e


b = BinaryTree()
b.insert(10)
b.insert(20)
b.insert(30)
b.insert(15)
b.insert(5)
b.insert(25)
b.insert(2)
b.traverse(mode=BinaryTree.PRE_ORDER)
b.delete(value=5)
b.traverse(mode=BinaryTree.IN_ORDER)
