class MaxHeap:
    """
    A class used to represent a max heap

    Attributes
    ----------
    heap : list
        A list representing the heap.

    size : int
        The size of our heap.

    Methods
    -------
    None
    """
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """
        Function to add item to our heap

        Parameters
        ----------
        value: int
            The value we want to add to our heap

        Returns
        -------
        None
        """
        self.heap.append(value)
        self.heapify_up()

    def extract_max(self):
        """
        Function get max value in our heap. If we have a max value and its
        not the only item in our heap then we will get the max value. set
        first element of the heap as the last element in our list. Then heapify
        This will ensure that our list remains a heap. 

        Parameters
        ----------
        None

        Returns
        -------
        int
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return max_value

    def heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

max_heap = MaxHeap()
max_heap.insert(50)
max_heap.insert(30)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(10)
max_heap.insert(8)

print(max_heap.heap) 
print(max_heap.extract_max()) 
print(max_heap.heap)  
