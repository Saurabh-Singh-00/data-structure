from collections import defaultdict, deque
from random import randint


class Graph:
    ''' 
    A Graph Data Structure using adjacency list representation.

    To create a graph object:
    g = Graph()

    To add a vertex:
    g.add_vertex(vertex)

    To add an edge between to vertices
    g.add_edge(source, target)
    '''

    def __init__(self, is_directed=False):
        self.adjacency_list = dict()
        self.is_directed = is_directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = set()

    def add_edge(self, source, target):
        self.get_neighbors(source).add(target)

        if not self.is_directed:
            self.get_neighbors(target).add(source)

    def remove_vertex(self, vertex):
        for v in self.adjacency_list.keys():
            self.get_neighbors(v).discard(vertex)
        del self.adjacency_list[vertex]

    def remove_edge(self, source, target):
        if not self.is_directed and target in self.adjacency_list:
            self.get_neighbors(target).discard(source)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def has_path(self, source, target):
        return target in self.get_neighbors(source)

    def __str__(self):
        return str(self.adjacency_list)

    def __repr__(self):
        return "Graph()"


class Paths:

    def depth_first_search(self, graph, start=None):
        stack = []
        path = []
        visited = defaultdict(lambda: False)
        stack.append(start)
        while len(stack) != 0:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                path.append(node)
            for v in graph.get_neighbors(node):
                if not visited[v]:
                    stack.append(v)
        return path

    def breadth_first_search(self, graph, start):
        q = deque()
        path = []
        visited = defaultdict(lambda: False)
        q.append(start)
        while len(q) != 0:
            node = q.popleft()
            if not visited[node]:
                visited[node] = True
                path.append(node)
            for v in graph.get_neighbors(node):
                if not visited[v]:
                    q.append(v)                    
        return path


g = Graph()

for i in range(7):
    g.add_vertex(i)

for i in range(15):
    g.add_edge(randint(0, 6), randint(i % 7, 6))

print(g)

p = Paths()
print(p.depth_first_search(g, 2))
print(p.breadth_first_search(g, 2))
