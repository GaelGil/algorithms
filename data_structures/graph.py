class Graph:
    """
    A class used to represent a graph with a dictionary

    Attributes
    ----------
    graph: dict
        The dictionary representing our graph

    Methods
    -------
    insert_node(self, node, neighbors)
        Insert a new node in the graph and its neighbors.
    insert_new_neighbor(self, node, neighbor)
        Insert a new neighbor to an existing node.
    contains(self, val)
        Check if there is a certain value in our graph
    contains_path(self, origin, destination, type_)
        Check if a certain node has a path to another node
    bfs(self)
        Preform breadth first search.
    dfs(self)
        Perform depth first search on graph.
    display(self)
        Return the dictionary that represents our graph.
    """
    def __init__(self) -> None:
        self.graph = {}

    def insert_node(self, node, neigbors=[]):
        """Function to insert a node and its neighbors into our graph. We
        first check that the node is not currently in our dictionary graph.
        Once we know its not we add a new key to our dictionary (node) and
        its value (neighbors).

        Parameters
        ----------
        node: int
            The node we are trying to add to our graph
        neighbors: list
            The list of neighbors to our node

        Returns
        -------
        None
        """

        if not self.contains(node):
            self.graph[node] = neigbors

    def insert_new_neighbor(self, node, neighbor):
        """Function to add a neighbor to an existing node. If that neighbor
        is already in the list of neighbors of that existing node. We don't
        add it. If its not an existing neighbor to that node we add it to
        the list of neighbors. We also add that new neighbor as a node with
        the `insert_node` function.

        Parameters
        ----------
        node: int
            Node we are trying to add a neighbor to.
        neighbor: int
            The neighbor we want to add to the node.

        Returns
        -------
        None
        """
        if neighbor in self.graph[node]:
            return
        self.graph[node].append(neighbor)
        if not self.contains(neighbor):
            self.insert_node(neighbor)


    def contains(self, val):
        """Function to check if we have a certain node in our dictionary graph.
        The time complexcity of this is O(1) because we to check for a
        dictionaries value its constant time.

        Parameters
        ----------
        val: int
            The value we are trying to check for.

        Returns
        -------
        bool
            True if the value is in the graph. False if it is not.
        """

        if val in self.graph:
            return True
        return False


    def contains_path(self, origin, destination, type_='dfs'):
        """Check if a node has a path to another node. First we check if
        the origin node and the destination node exist. If they do not
        theres no way a path could exist. 

        Parameters
        ----------
        origin : node
            The origin where we start at.
        destination : node
            The destination node
        type_ : str, optional
            A string to pick which type of traversal to use(default is
            dfs)

        Returns
        -------
        list
            a list of strings used that are the header columns
        """

        if self.contains(origin) is False or self.contains(origin) is False:
            return f'One of the nodes is not in the graph'
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
        """Function to perform breadth first traversal. In breadth first
        traversal we get all the nodes neighbors and keep exploring other
        nodes from those nodes. We do this by starting at some node adding
        its neighbors to a queue. Then we select the node at the beggining
        of our queue to remove but to also traverse their nodes by adding
        them to the queue. We repeate this until we cant anymore. We also
        use a dictionary to check which nodes we have visited so we don't
        repeate forever.

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
            current_node = queue.pop()
            print(current_node)
            if current_node not in visited and current_node in self.graph:
                visited[current_node] = 0
                for i in self.graph[current_node]:
                    queue.insert(0, i)
        return visited

    def dfs(self, node):
        """Function that performs depth first search. In depth first search
        once we have a node we have to explore all its other nodes until we
        can continue exploring other nodes and their nodes. We do this by
        starting at some node adding its neighbors to a stack. Then we select
        the node at the top of our stack to remove but to also traverse their
        nodes. We repeate this until we cant anymore. We also use a dictionary
        to check which nodes we have visited so we don't repeate forever.

        Parameters
        ----------
        node: int
            The node to start our depth first traversal at

        Returns
        -------
        dict
            All the other nodes we were able to visit by starting at
            our node.
        """
        stack = [node]
        visited = {}
        while stack:
            current_node = stack.pop()
            # print(node)
            if current_node not in visited and current_node in self.graph:
                visited[current_node] = 0
                for i in self.graph[current_node]:
                    stack.append(i)
        return visited


    def display(self):
        """Return the dictionary graph.

        Parameters
        ----------
        None

        Returns
        -------
        dict
            The dictionary that represents our graph.
        """
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


