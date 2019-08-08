class BinaryTree:

    IN_ORDER, PRE_ORDER, POST_ORDER = 0, 1, 2

    class Node:
        def __init__(self, data):
            self.data = data
            self.l_child = None
            self.r_child = None

        def __str__(self):
            if BinaryTree.PRE_ORDER:
                return "{{Node: {{data: {}, left: {}, right: {} }}}}".format(self.data, self.l_child, self.r_child)
            elif BinaryTree.IN_ORDER:
                return "{{Node: {{left: {}, data: {}, right: {} }}}}".format(self.l_child, self.data, self.r_child)
            elif BinaryTree.POST_ORDER:
                return "{{Node: {{left: {}, right: {}, data: {} }}}}".format(self.l_child, self.r_child, self.data)

    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            _ = self.root
            _root = _
            while _:
                _root = _
                if data < _.data:
                    _ = _.l_child
                else:
                    _ = _.r_child
            if data < _root.data:
                _root.l_child = self.Node(data)
            else:
                _root.r_child = self.Node(data)

    def traverse(self, mode):
        if mode == BinaryTree.IN_ORDER:
            BinaryTree.IN_ORDER, BinaryTree.PRE_ORDER, BinaryTree.POST_ORDER = True, False, False
        elif mode == BinaryTree.PRE_ORDER:
            BinaryTree.IN_ORDER, BinaryTree.PRE_ORDER, BinaryTree.POST_ORDER = False, True, False
        elif mode == BinaryTree.POST_ORDER:
            BinaryTree.IN_ORDER, BinaryTree.PRE_ORDER, BinaryTree.POST_ORDER = False, False, True
        print(self.root)

    def search(self, value):
        if self.root is None:
            raise Exception("Value {} does not exists".format(value))
        _ = self.root
        while _ is not None and value != _.data:
            if value < _.data:
                _ = _.l_child
            else:
                _ = _.r_child
        if _ is None:
            raise Exception("Value {} does not exists".format(value))
        print("Value {} exists".format(value))

    def delete(self, value):
        # TODO: Implement Delete
        pass


b = BinaryTree()
b.insert(10)
b.insert(20)
b.insert(30)
b.insert(15)
b.insert(5)
b.insert(25)
b.traverse(mode=BinaryTree.POST_ORDER)
b.search(value=26)
