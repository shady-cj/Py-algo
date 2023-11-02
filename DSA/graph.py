# Implement a graph


# class Node:
#     def __init__(self, value):
#         self.value = value

#     def __repr__(self):
#         return str(self.value)


class UnDirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def insert(self, value):
        if value not in self.adjacency_list:
            self.adjacency_list[value] = set([])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].add(vertex2)
            self.adjacency_list[vertex2].add(vertex1)


new_graph = UnDirectedGraph()

new_graph.insert(4)
new_graph.insert(10)
new_graph.insert(14)


new_graph.add_edge(4, 10)
new_graph.insert(4)
print(new_graph.adjacency_list)


class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def insert(self, value):
        if value not in self.adjacency_list:
            self.adjacency_list[value] = set([])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].add(vertex2)


new_graph = DirectedGraph()

new_graph.insert(4)
new_graph.insert(10)
new_graph.insert(14)


new_graph.add_edge(4, 10)
new_graph.insert(4)
new_graph.add_edge(10, 4)
print(new_graph.adjacency_list)
