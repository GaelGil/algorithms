from node import Node


class LinkedList:
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
        self.head = Node()
        self.size = 0

    def append(self, data) -> None:
        # TODO: finish docuementation
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
        new_node = Node(data)
        if self.head.val == None:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.size += 1
        return

    def add_infront(self, data) -> None:
        # TODO: finish docuementation
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
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return

    def display(self) -> list:
        # TODO: finish docuementation
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
        items = []
        current = self.head
        while current:
            items.append(f'{current.val} ->')
            current = current.next
        return items

    def get_head(self):
        # TODO: finish docuementation
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
        return self.head

    def get_last(self):
        # TODO: finish docuementation
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
        current = self.head
        while current.next != None:
            current = current.next
        return current


    def get_item(self, item):
        # TODO: finish docuementation
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
        current = self.head
        while current:
            if current.val == item:
                return 'Found'
            current = current.next
        return 'Not Found'

    def get_index(self, index):
        # TODO: finish docuementation
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
        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                return current
            current_index += 1
            current = current.next
        return 'Index Out of Range'

    def get_size(self):
        return self.size


    def sum(self):
        # TODO: finish docuementation
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
        sum_ = 0
        current = self.head
        while current:
            sum_ += current.val
            current = current.next
        return sum_

    def delete(self, item):
        # TODO: finish docuementation
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
        current = self.head
        prev = self.head
        while current:
            if item == current.val:
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        return f'{item} not found'


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

print(list.get_item(2))
print(list.get_item(6))

print(list.get_index(5).val)
print(list.get_index(7))

list.delete(2)

print(list.display())

print('sum')
print(list.sum())

print('size')
print(list.get_size())
