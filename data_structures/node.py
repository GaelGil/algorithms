class Node:
    """
    A class used to represent a single node.

    Attributes
    ----------
    val : int
        Value of the node
    next : node
        The address of the next node (set to None by default)

    Methods
    -------
    None
    """
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None