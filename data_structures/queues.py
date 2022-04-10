from node import Node

class Queue:
    """
    A class used to represent a queue with nodes.

    Attributes
    ----------
    head : node
        The node at the front of our queue.
    tail: node
        The node at the end of our queue.

    Methods
    -------
    enqueue(self, data)
        Insert node at the top of our stack.
    dequeue(self, data, current_node)
        Remove the top node from the stack.
    display(self)
        Get our queue in a list format
    get_head(self)
        Get the head of queue.
    get_tail(self)
        Get the tail of our queue.
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Add a node to our queue.

        Parameters
        ----------
        data: node
            Node we want add to our queue.

        Returns
        -------
        None
        """
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        return

    def dequeue(self):
        """

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        return

    def display(self):
        """Function to return a list containing all the values of the 
        nodes in our queue.
        The time complexity of this is O(n) because we have to iterate through
        all the nodes in our queue and add them to a list.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of the nodes in our queue
        """
        items = []
        current = self.head
        while current:
            items.append(current.val)
            current = current.next
        return items

    def get_head(self):
        """Return the head node of our queue.

        Parameters
        ----------
        None

        Returns
        -------
        node
            The node in the front of the queue.
        """
        return self.head

    def get_tail(self):
        """Return the tail node of our queue.

        Parameters
        ----------
        None

        Returns
        -------
        node
            The node at the front of the queue.
        """
        return self.tail

print('Node Implementation')
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.dequeue()


print(f'Display: {q.display()}')
print(f'Head: {q.get_head().val}')
print(f'tail: {q.get_tail().val}')
print()
print()



class QueueList:
    """
    A class used to represent a stack with nodes

    Attributes
    ----------
    top : node
        The node at the top of the stack

    Methods
    -------
    push(self, data)
        Insert node at the top of our stack
    pop(self, data, current_node)
        Remove the top node from the stack
    get_top(self)
        Return the top of the stack.
    is_empty(self)
        Check if the stack is empty.
    display(self)
        Get the sum of the tree.
    """
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
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
        self.queue.insert(0, data)
        return 

    def dequeue(self):
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
        self.queue.pop()
        return

    def get_head(self):
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
        return self.queue[-1]

    def get_tail(self):
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
        return self.queue[0]

    def get_lenght(self):
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
        return len(self.queue)

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
        return self.queue


q = QueueList()
q.enqueue(1)
q.enqueue(12)
q.enqueue(23)
q.enqueue(34)
q.enqueue(45)
q.enqueue(56)
q.enqueue(67)
q.enqueue(78)


print(f'List Implementation')
print(f'Head: {q.get_head()}')
print(f'Tail: {q.get_tail()}')
print(f'Queue: {q.display()}')
print()
q.dequeue()
q.dequeue()
q.dequeue()
print(f'Head: {q.get_head()}')
print(f'Tail: {q.get_tail()}')
print(f'Queue: {q.display()}')