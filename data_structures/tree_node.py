class Node:
    """
    A class used to represent a single node in a binary tree.
    Its attributes are the address the left and right node as well as 
    the value. 

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