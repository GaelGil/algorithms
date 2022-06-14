class DoublyLinkedNode:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    A class used to represent a singly linked list.

    Attributes
    ----------
    head: node
        The head node of the linked list
    size: int
        The size of the linked list (how many items are in our list)

    Methods
    -------
    append(self, data)
        Function to add new node at the end of the list.
    preppend(self, data)
        Function to add a new node at the front of doubly linked list.
    insert_at_index(self)
        Function to insert a node at a certain index in a doubly linked list. 
    pop(self, left)
        Function to pop left or right from the doubly linked list.
    delete_at_index(self, index)
        Delete the node at a specified index in the list.
    display(self, item)
        Return a list of the elements in the doubly linked list.
    get_tail(self)
        Return the tail node of the list.
    get_head(self)
        Return the head node of the list.
    get_index(self, index)
        Get node in list by index.
    get_value(self, val)
        Get a node in the doubly linked list by value
    get_size(self)
        Get the size of the doubly linked list.
    """
    def __init__(self) -> None:
        self.head = DoublyLinkedNode(val=None)
        self.tail = DoublyLinkedNode(val=None, prev=self.head, next=self.head)
        self.size = 0

    def append(self, data):
        """Add another node at the end of our linked list. If our head
        is empty we set our head to be equal to our new node. We also
        increase the size of our linked list so we add that. Then we return
        If our head is not empty we iterate all the way to the end of the list
        until we get to the last node. We set the last nodes next value to be
        our new node. We also increase our size by 1
        If our head is empty the time complexcity to add is O(1).
        If our head is not empty the time complexcity is O(n) because we have to
        iterate the whole list to get to the end to add.

        Parameters
        ----------
        data: int
            The value we are trying to store in our linked list

        Returns
        -------
        None
        """
        new_node = DoublyLinkedNode(data)
        if not self.head.next:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail.prev = new_node
        else:
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev = new_node
        self.size += 1

    def preppend(self, data):
        """Add a node to the beggining of our linked list.
        The time complexcity of this is O(1) because we have access to the head.

        Parameters
        ----------
        data: int
            The value we are trying to store in our linked list

        Returns
        -------
        None
        """
        new_node = DoublyLinkedNode(data)
        if not self.head.next:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail.prev = new_node
        else:
           new_node.prev = self.head
           new_node.next = self.head.next
           self.head.next.prev = new_node
           self.head.next = new_node
           self
        self.size += 1

    def insert_at_index(self, index, value):
        """
        Function to insert a node at a certain index in a doubly linked list.
        If the index we want to add is greater than the size of our list we
        return false. We create a current index variable and iterate the list.
        Once we arrive at the index we want we assign the correct directions.
        The new nodes previous points to the current node and the next points
        to the currents next. Then the currents next previous points to the new
        node. Lastly the current nodes next points to the new node.

        Parameters
        ----------
        index : int
            The index we want to add our new node to.

        value : int
            The value of our new node

        Returns
        -------
        None
        """
        if index > self.size:
            return False
        current_index = 0
        current = self.head
        new_node = DoublyLinkedNode(value)
        while current:
            if current_index == index:
                new_node.prev = current
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
            current_index += 1

    def pop(self, left=False):
        """Pop from left or right of our doubly linked list. By default we pop
        from the right. What we do is make the `tails prev` node point to
        `tails prev prev` node. Lastly because the tails previous node is already
        the the prev prev. We make that nodes next point to our next.
        If we want to pop from the left we do something similar. What we do is
        make `head next` point to `head next next`. Then we make that node point back
        the head as its previous.

        Parameters
        ----------
        left: bool
            Bool to see if we want to pop left or right of the list.
            (set to False as default)

        Returns
        -------
        None
        """
        if not left:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
        if left:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

    def delete_at_index(self, index):
        """Delete a node in a doubly linked list by index in the list. 
        The time complexcity of this is O(n) because we have to iterate
        through the list to get to any index.

        Parameters
        ----------
        index : int
            The index of the node we want to delete

        Returns
        -------
        None
        """
        if index > self.size:
            return
        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = None
                return
            current = current.next


    def display(self):
        """Gets all the elements in our linked list and returns them as
        a regular list.
        The time complexcity of this is O(n) because we have to iterate
        through the whole list and add the items to our list.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list containing the values of the nodes in our linked list
        """
        current = self.head
        items = []
        while current:
            items.append(current.val)
            current = current.next
            if current == self.tail:
                items.append(current.val)
                current = None
        return items

    def get_tail(self):
        """Return the tail node of the linked list

        Parameters
        ----------
        None

        Returns
        -------
        node
            The tail node.
        """
        return self.tail

    def get_head(self):
        """Return the head node of the linked list

        Parameters
        ----------
        None

        Returns
        -------
        node
            The head node.
        """
        return self.head

    def get_index(self, index):
        """Return the node at the specified index in our list.

        Parameters
        ----------
        index : int
            The index at our linked lists which node we want.

        Returns
        -------
        Node
            The node at that index in our list. (false if doesnt exist)
        """
        if index > self.size:
            return False
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                return current
            current = current.next
            current_index += 1


    def get_value(self, val):
        """Return the node which has the same value as we want in our list.

        Parameters
        ----------
        val : int
            The value of a node in our linked lists which node we want.

        Returns
        -------
        Node
            The node which matches a value in our list. (false if doesnt exist)
        """
        current = self.head
        while current:
            if current.val == val:
                return current.val
            current = current.next
        return f'Value {val} not in list'


    def get_size(self):
        """Return the size of the linked list. The size is a class variable
        that is update everytime we add and delete to our list.

        Parameters
        ----------
        None

        Returns
        -------
        int
            Size of the linked list
        """
        return self.size


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(7)
dll.append(8)
dll.append(9)
dll.append(10)
dll.preppend(0)
dll.preppend(-1)
dll.preppend(-2)
dll.preppend(-3)


print(dll.get_size())
print(dll.display())
# dll.display()
dll.pop()
print(dll.display())

dll.pop(left=True)
print(dll.display())
