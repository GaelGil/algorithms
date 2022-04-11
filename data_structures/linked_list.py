from node import Node


class LinkedList:
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
        self.head = Node()
        self.size = 0

    def append(self, data) -> None:
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
        new_node = Node(data)
        if not self.head.val:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size += 1
        return

    def add_infront(self, data):
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
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def display(self) -> list:
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
        items = []
        current = self.head
        while current:
            items.append(f'{current.val} ->')
            current = current.next
        return items

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

    def get_last(self):
        """Return the node at the end of the list. Iterate the list until we get to the end.
        Then we can return that node.

        Parameters
        ----------
        None

        Returns
        -------
        node
            The last node in our list.
        """
        current = self.head
        while current.next is not None:
            current = current.next
        return current


    def includes(self, item):
        """Check if a certain item exists in our linked list. To do this we iterate
        the whole list checking for the value.
        The time complexcity of this is O(n) because in the worst case scenario we
        have to iterate throug the whole list to find our value.

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
        current = self.head
        while current:
            if current.val == item:
                return 'Found'
            current = current.next
        return 'Not Found'

    def get_index(self, index):
        """Return the node at the index we want.
        The time complexity of this is O(n) where n is the index of the
        node we are trying to delete. It's O(n) because we have to iterate
        the list to get to that position. It's not a regular list where we
        can access by index.

        Parameters
        ----------
        index: int
            The index of the node we are trying to find

        Returns
        -------
        node
            The node at the index we wanr
        """
        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                return current
            current_index += 1
            current = current.next
        return 'Index Out of Range'

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


    def sum(self):
        """Return the sum of the values in our linked list. To do this
        we iterate the whole list adding the values of the nodes to a
        counter. We then return the counter (sum_).
        The time complexcity of this is O(n) because we have to iterate
        the whole list to get the sum.

        Parameters
        ----------
        None

        Returns
        -------
        int
            The sum of the values in our linked list.
        """
        sum_ = 0
        current = self.head
        while current:
            sum_ += current.val
            current = current.next
        return sum_

    def delete(self, value):
        """Delets a node in our list by value. We do this iterating through
        our list and keeping track of the previous node we go through the
        list. If we find our value in the list we set our previous node next
        value to the node we are trying to delete's next value.
        The time complexcity of this is O(n) because we have to iterate through
        the whole list in worset case scenario.

        Parameters
        ----------
        value: int
            The value we are trying to delete from our linked list

        Returns
        -------
        str
            A string saying `value not found` if its not in our linked list.
        """
        current = self.head
        prev = self.head
        while current:
            if value == current.val:
                prev.next = current.next
                self.size -= 1
                return f'Delete {value}'
            prev = current
            current = current.next
        return f'{value} not found'


list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print(list.display())


# print(list.get_head().val)


list.add_infront(0)
print(list.display())


# print(list.get_last().val)

print(list.includes(2))
print(list.includes(6))

print(list.get_index(5).val)
print(list.get_index(7))

list.delete(2)

print(list.display())

print('sum')
print(list.sum())

print('size')
print(list.get_size())
