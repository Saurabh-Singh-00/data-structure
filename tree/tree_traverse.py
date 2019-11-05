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
    from stack.stack import Stack


class TreeTraverse:

    IN_ORDER: int = 0
    PRE_ORDER: int = 1
    POST_ORDER: int = 2

    def breadth_first_search(self, node):
        if node is None:
            return
        queue = Queue()
        visited = SinglyLinkedList()
        queue.enqueue(node)
        while not queue.is_empty:
            node = queue.dequeue().data
            visited.append(node.data)
            if node.l_child:
                queue.enqueue(node.l_child)
            if node.r_child:
                queue.enqueue(node.r_child)
        return visited

    def __pre_order(self, node: BinaryTree.Node, path: SinglyLinkedList):
        if node is None:
            return
        path.append(node.data)
        if node.l_child:
            self.__pre_order(node.l_child, path)
        if node.r_child:
            self.__pre_order(node.r_child, path)
        return path

    def __in_order(self, node: BinaryTree.Node, path: SinglyLinkedList):
        if node is None:
            return
        if node.l_child:
            self.__in_order(node.l_child, path)
        path.append(node.data)
        if node.r_child:
            self.__in_order(node.r_child, path)
        return path

    def __post_order(self, node: BinaryTree.Node, path: SinglyLinkedList):
        if node is None:
            return
        if node.l_child:
            self.__post_order(node.l_child, path)
        if node.r_child:
            self.__post_order(node.r_child, path)
        path.append(node.data)
        return path

    def depth_first_search(self, node, mode):
        traversed = SinglyLinkedList()
        if node is None:
            return
        if mode is TreeTraverse.PRE_ORDER:
            self.__pre_order(node, traversed)
        elif mode is TreeTraverse.IN_ORDER:
            self.__in_order(node, traversed)
        elif mode is TreeTraverse.POST_ORDER:
            self.__post_order(node, traversed)
        return traversed


b = BinaryTree()
b.insert(10)
b.insert(6)
b.insert(15)
b.insert(3)
b.insert(8)
b.insert(20)
traverse = TreeTraverse()
print(traverse.breadth_first_search(b.root))
print(traverse.depth_first_search(b.root, TreeTraverse.PRE_ORDER))
print(traverse.depth_first_search(b.root, TreeTraverse.IN_ORDER))
print(traverse.depth_first_search(b.root, TreeTraverse.POST_ORDER))
