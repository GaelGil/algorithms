from importlib.resources import path
from operator import contains, truediv


class Graph:
    def __init__(self) -> None:
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a'],
            'c': ['e', 'f'],
            'd': ['c', 'e'],
            'e': ['f', 'g'],
            'f': ['g', 'e'],
            'g': []
        }


    def insert_node(self, node):
        return

    def contains(self, val):
        if val in self.graph:
            return True
        return False

    def contains_path(self, origin, destination, type_):
        if self.contains(origin) == False:
            return f'{origin} not in graph'
        if type_ == 'dfs':
            visited = self.dfs(origin)
            if visited and destination in visited:
                return True
        else:
            visited = self.bfs(origin)
            if visited and destination in visited:
                return True
        return False


    def bfs(self, node):
        queue = [node]
        visited = {}
        while queue:
            n = queue.pop()
            # print(n)
            if n not in visited:
                visited[n] = 0
                for i in self.graph[n]:
                    queue.insert(0, i)
        return visited

    def dfs(self, node):
        stack = [node]
        visited = {}
        while stack:
            node = stack.pop()
            # print(node)
            if node not in visited:
                visited[node] = 0
                for i in self.graph[node]:
                    stack.append(i)
        return visited


    

# graph = {
#     'a': ['b', 'c', 'd'],
#     'b': ['a'],
#     'c': ['e', 'f'],
#     'd': ['c', 'e'],
#     'e': ['f', 'g'],
#     'f': ['g', 'e'],
#     'g': []
# }

g = Graph()

print(g.contains('a'))
print(g.contains('j'))

path_g_to_a = g.contains_path('g', 'a','dfs')
print()
path_a_to_g = g.contains_path('a', 'g','dfs')

print(f'Does g contain some path to a: {path_g_to_a}')
print(f'Does a contain some path to g: {path_a_to_g}')



