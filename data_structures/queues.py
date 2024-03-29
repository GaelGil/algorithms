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
        """Add a node to our queue. If we don't have a head or tail node. Then the first value
        we add to our list will be our head and tail node. Moving forward since we have a tail
        we will set the tail.next to point to our new node. Also setting our new node to the tail.
        The time complexcity of this is O(1) because we have access to the tail node so we just
        assign a next node to the current tail and reassign the tail value to our new node.

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
        """Dequeue a node from our list. If we have a head node we want to check if it is
        the only node in the list. If it is we set our head and tail node to equal None.
        If we have more than one node then we set the head node to the current head.next node.
        The time complexity of this is O(1) because we simply just reassign our head node to
        the next node.
    
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
    A class used to represent a queue with nodes.

    Attributes
    ----------
    queue: list
        The list representing our queue.

    Methods
    -------
    enqueue(self, data)
        Insert node at the top of our stack.
    dequeue(self, data, current_node)
        Remove the top node from the stack.
    get_head(self)
        Get the head of queue.
    get_tail(self)
        Get the tail of our queue.
    get_length(self)
        Get the lenght of the queue
    display(self)
        Get our queue in a list format
    """
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
        """Insert a value at position 0 of our queue list. This way what we first
        added will always be at the last index of our list.
        The time complexcity of this is O(n) because although we are inserting at
        a given index we are also shifting all the elements in the array one up.

        Parameters
        ----------
        data: int
            The value we want to insert into our queue list.

        Returns
        -------
        None
        """
        self.queue.insert(0, data)
        return 

    def dequeue(self):
        """Removes the value at the last index in our list.
        The time complexcity of this is O(1) because we have the index of where we want
        to remove.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.queue.pop()
        return

    def get_head(self):
        """Returns the item at the last index of our list. This is the head of
        our queue.
        The time complexcity of this is O(1) because we have the index of where the
        head is.

        Parameters
        ----------
        None

        Returns
        -------
        int
            The integer at the front of our queue list.
        """
        return self.queue[-1]

    def get_tail(self):
        """Returns tha item at the 0th index of our list. This is the tail of our
        queue list.
        The time complexcity of this is O(1) because we have the index of where the
        tail is.

        Parameters
        ----------
        None

        Returns
        -------
        int
            The integer at the back of our queue list.
        """
        return self.queue[0]

    def get_lenght(self):
        """Returns the length of our queue.

        Parameters
        ----------
        None

        Returns
        -------
        int
            The lenght of our queue.
        """
        return len(self.queue)

    def display(self):
        """Returns our queue list.

        Parameters
        ----------
        None

        Returns
        -------
        list
            The queue list.
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