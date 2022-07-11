class Heap:
    """
    A class used to represent a heap

    Attributes
    ----------
    heap_list : list
        A list representing the heap.

    size : int
        The size of our heap.

    Methods
    -------
    None
    """
    def __init__(self) -> None:
        self.heap_list = []
        self.size = 0

    def peek(self):
        """
        Function to return the value at the top of our heap.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        return self.heap_list[0]

    def poll(self):
        """
        Function to return the value at the top of our heap.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.heap_list:
            self.heap_list().pop(0)
        return False

    def add(self, value):
        """
        Function to return the value at the top of our heap.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.heap_list.append(value)
        self.heapify_down

    def heapify_down(self):
        """
        Function to return the value at the top of our heap.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        return
    
    def heapify_up(self):
        """
        Function to return the value at the top of our heap.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        return


heap = Heap()
