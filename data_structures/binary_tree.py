class Node:
    """
    A class used to represent a single node

    Attributes
    ----------
    val : int
        Value of the node
    left : node
        The address of the left node (set to None by default)
    right: node
        The address of the right noed (set to None by default)

    Methods
    -------
    None
    """
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Tree:
    """
    A class used to represent a single node

    Attributes
    ----------
    val : int
        Value of the node
    left : node
        The address of the left node (set to None by default)
    right: node
        The address of the right noed (set to None by default)

    Methods
    -------
    insert(self, data)
        Insert node into the three

    _insert(self, data, current_node)
        Find the correct spot to insert our node in the tree
    
    get_root(self)
        return the root of out tree
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
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
        if not self.root:
            new_node = Node(data)
            self.root = new_node
            return
        self._insert(data, self.root)

    def _insert(self, data, current_node):
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
        if data < current_node.val:
            if not current_node.left:
                current_node.left = Node(data)
                return
            else:
                self._insert(data, current_node.left)
                return
        if data >= current_node.val:
            if not current_node.right:
                current_node.right = Node(data)
                return
            else:
                self._insert(data, current_node.right)
        return

    def get_root(self):
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
        return self.root

    def includes(self):
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

    def sum(self):
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

    def _min(self):
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

    def _max(self):
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

    def in_order(self):
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
        if self.root:
            self._in_order(self.root) 
        return 

    def _in_order(self, node):
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
        if node:
            self._in_order(node.left)
            print(node.val)
            self._in_order(node.right)
        return

    def pre_order(self):
        """ 
        like depth first search (explore all the nodes and their paths then go back and explore others) 
        """
        if self.root:
            self._pre_order(self.root)
        return

    def _pre_order(self, node):
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
        if node:
            print(node.val)
            self._pre_order(node.left)
            self._pre_order(node.right)
        return

    def post_order(self):
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
        if self.root:
            self._post_order(self.root)
        return

    def _post_order(self, node):
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
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.val)
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
        queue = [self.root]
        while queue:
            node = queue.pop()
            print(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return


tree = Tree()
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(5)
tree.insert(12)


print()
tree.in_order()

print()
tree.post_order()

print()
tree.pre_order()

print()
tree.bfs()

# In depth first search if you have a node you must visit all the other nodes on that node until it
# has no connections before moving on. Uses stack data structure.
# In breadth first search you check all nodes at once until you can't check anymore. Uses queue data
# structure

# Implement dfs and bfs in trees 