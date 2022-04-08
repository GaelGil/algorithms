class Graph:
    """
    A class used to represent a single node

    Attributes
    ----------
    val : int
        Value of the node
    next : node
        The address of the next node

    Methods
    -------
    None
    """
    def __init__(self) -> None:
        self.graph = {}

    def insert_node(self, node, neigbors):
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is
            False)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """

        if not self.contains(node):
            self.graph[node] = neigbors            
        return

    def insert_new_neighbor(self, node, neighbor):
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is
            False)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """

        for i in self.graph[node]:
            if i == neighbor:
                return
        self.graph[node].append(neighbor)
        

    def contains(self, val):
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is
            False)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """

        if val in self.graph:
            return True
        return False

    def contains_path(self, origin, destination, type_):
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is
            False)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """

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
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is
            False)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """
    
        queue = [node]
        visited = {}
        while queue:
            n = queue.pop()
            # print(n)
            if n not in visited and node in self.graph:
                visited[n] = 0
                for i in self.graph[n]:
                    queue.insert(0, i)
        return visited

    def dfs(self, node):
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is
            False)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """

        stack = [node]
        visited = {}
        while stack:
            node = stack.pop()
            # print(node)
            if node not in visited and node in self.graph:
                visited[node] = 0
                for i in self.graph[node]:
                    stack.append(i)
        return visited


    def display(self):
        return self.graph

    

# graph = {
#     'a': ['b', 'c', 'd', 'l'],
#     'b': ['a'],
#     'c': ['e', 'f'],
#     'd': ['c', 'e'],
#     'e': ['f', 'g'],
#     'f': ['g', 'e'],
#     'g': []
# }

g = Graph()

g.insert_node('a', ['b', 'c', 'd'])
g.insert_node('b', ['a'])
g.insert_node('c', ['e', 'f'])
g.insert_node('d', ['c', 'f'])
g.insert_node('e', ['f', 'g'])
g.insert_node('f', ['g', 'e'])
g.insert_node('g', [])
print(g.display())
print()
g.insert_new_neighbor('a', 'l')
print(g.display())
print()

print(g.contains('a'))
print(g.contains('j'))

path_g_to_a = g.contains_path('g', 'a','dfs')
print()
path_a_to_g = g.contains_path('a', 'g','dfs')

print(f'Does g contain some path to a: {path_g_to_a}')
print(f'Does a contain some path to g: {path_a_to_g}')




