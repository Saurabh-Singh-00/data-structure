try:
    from linked_list.abstract_node import AbstractNode
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.path.pardir)))
    from linked_list.abstract_node import AbstractNode
    from linked_list.singly_linked_list import SinglyLinkedList
    from tqueue.queue import Queue
    from tree.binary_tree import BinaryTree


class TreeTraverse:

    queue = Queue()
    visited = SinglyLinkedList()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def breadth_first_search(cls, node):
        ''' Use it as \n
        binary_tree = BinaryTree()\n
        TreeTraverse.breadth_first_search(binary_tree.root) \n
        '''
        if node is None:
            return
        cls.queue.enqueue(node)
        while not cls.queue.is_empty:
            node = cls.queue.dequeue().data
            cls.visited.append(node.data)
            if node.l_child:
                cls.queue.enqueue(node.l_child)
            if node.r_child:
                cls.queue.enqueue(node.r_child)
        return cls.visited


b = BinaryTree()
b.insert(10)
b.insert(6)
b.insert(15)
b.insert(3)
b.insert(8)
b.insert(20)
print(TreeTraverse.breadth_first_search(b.root))
