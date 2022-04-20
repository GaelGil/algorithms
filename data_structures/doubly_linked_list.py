class DoublyLinkedNode:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    # TODO: finish documentation
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
        Insert node at the top of our stack.
    add_infront(self, data)
        Remove the top node from the stack.
    display(self)
        Get the sum of the tree.
    get_head(self)
        Return the head node of the linked list.
    get_last(self)
        Return the node at the end of the linked list.
    includes(self, item)
        Check if linked list contains an item.
    get_index(self, index)
        Get a node in the linked list by index.
    get_size(self)
        Return the size of the linked list.
    sum(self)
        Return the sum of the items in our linked list.
    delete(self, item)
        Delete and item if it is in our list
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
        return

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
        return

    def insert_after_value(self, value):
        return

    def insert_at_index(self, index):
        return 

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
            return
        if left:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            return

    def delete(self):
        return

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
        return

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
        return


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