class Node:
    """
    A class used to represent a single node

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

class LinkedList:
    """
    A class used to represent a single node

    Attributes
    ----------
    val : int
        Value of the node
    next : node
        The address of the next node

    Methods
    -------
    None
    """
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data) -> None:
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
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def add_infront(self, data) -> None:
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

    def display(self) -> list:
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

    def get_length(self):
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
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def get_last(self):
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


    def sum(self):
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

print('length')
print(list.get_length())
print()

print('sum')
print(list.sum())
