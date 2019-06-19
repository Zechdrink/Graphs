# Definition for a binary tree node.

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist")

#     def earliest_ancestor(self, start):
#         stack = Stack()
#         stack.push([start])
#         visited = set()
#         new_path = None
#         while stack.size() > 0:
#             path = stack.pop()
#             node = path[-1]
#             if node not in visited:
#                 visited.add(node)
#                 for next_node in self.vertices[node]:
#                     new_path = path.copy()
#                     new_path.append(next_node)
#                     stack.push(new_path)
        
#         return new_path[-1]



# if __name__ == '__main__':
#     graph = Graph()
#     graph.add_vertex(10)
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(4)
#     graph.add_vertex(11)
#     graph.add_vertex(3)
#     graph.add_vertex(5)
#     graph.add_vertex(8)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_vertex(9)
#     graph.add_edge(10, 1)
#     graph.add_edge(1, 3)
#     graph.add_edge(2, 3)
#     graph.add_edge(3, 6)
#     graph.add_edge(5, 6)
#     graph.add_edge(5, 7)
#     graph.add_edge(4, 5)
#     graph.add_edge(4, 8)
#     graph.add_edge(11, 8)
#     graph.add_edge(8, 9)

# print("")
# print(graph.earliest_ancestor(9))
# print("")

def earliest_ancestor(ancestors, start):
    #build graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        #build edges in reverse
        graph.add_edge(pair[1], pair[0])
    
    max_path_len = 1
    earliest_ancestor = -1

    s = Stack()
    s.push([start])
    while s.size > 0:
        path = s.pop()
        v = path[-1]

        if (len(path) == max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            

    
