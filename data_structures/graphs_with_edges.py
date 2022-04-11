class Graph:
    """
    A class used to represent a graph with edges. We do this with
    a dictionary.

    Attributes
    ----------
    graph: dict
        The dictionary representing our graph

    Methods
    -------
    insert_node(self, node, neighbors)
        Insert a new node in the graph and its neighbors.
    insert_neighbor_of_node(self, node, neighbor)
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


    def insert_node(self, node, neighbors=[]):
        # TODO: finish docuementation
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
        if node in self.graph:
            return
        self.graph[node] = neighbors
        return


    def insert_neighbor_of_node(self, node, neighbor):
        # TODO: finish docuementation
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
        if not node in self.graph:
            return
        for i in self.graph[node]:
            if neighbor[0] == i[0]:
                return
        self.graph[node].append(neighbor) 
        return


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
        # TODO: finish docuementation
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
        node : node
            The node where we start traversal

        Returns
        -------
        visited
            All the nodes we visited during traversal starting at our node.
        """

        queue = [node]
        visited = {}
        while queue:
            current_node = queue.pop()
            # print(n)
            if current_node not in visited and current_node in self.graph:
                visited[node] = 0
                for i in self.graph[current_node]:
                    queue.insert(0, i)
        return visited


    def dfs(self, node):
        # TODO: finish docuementation
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
        # TODO: finish docuementation
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
