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


    def insert_node(self, node, neighbors=[]):
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


    def bfs(self):
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
        return


    def dfs(self):
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
        return


    def display(self):
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
