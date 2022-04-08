class Graph:
    def __init__(self) -> None:
        self.graph = {}


    def insert_node(self, node, neighbors=[]):
        if node in self.graph:
            return
        self.graph[node] = neighbors
        return


    def insert_neighbor_of_node(self, node, neighbor):
        if not node in self.graph:
            return
        for i in self.graph[node]:
            if neighbor[0] == i[0]:
                return
        self.graph[node].append(neighbor)        
        return


    def bfs(self):
        return


    def dfs(self):
        return


    def display(self):
        return self.graph


g = Graph()



g.insert_node('a', [['b', 1], ['c', 5], ['d', 2]])
g.insert_node('b')
g.insert_node('c', [['e', 3], ['f', 4]])
g.insert_node('d', [['c', 2 ], ['f', 6]])
g.insert_node('e', [['f', 3], ['g', 1]])
g.insert_node('f', [['g', 4]])
g.insert_node('g', [])
print(g.display())
print()
g.insert_neighbor_of_node('g', ['b', 1])
print(g.display())
