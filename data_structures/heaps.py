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
        return self.heap_list[0]

    def poll(self):
        if self.heap_list:
            self.heap_list().pop(0)
        return False

    def add(self, value):
        self.heap_list.append(value)
        self.heapify_down

    def heapify_down(self):
        return
    
    def heapify_up(self):
        return


heap = Heap()
