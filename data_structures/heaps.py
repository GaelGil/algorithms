class Node:
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
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Heap:
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
        self.root = None

    def insert(self):
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

    def _insert(self):
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

    def dfs(self):
        return