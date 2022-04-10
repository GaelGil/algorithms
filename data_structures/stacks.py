from node import Node


class Stack:
    """
    A class used to represent a stack with nodes.

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
    peek(self)
        Return the top of the stack.
    is_empty(self)
        Check if the stack is empty.
    display(self)
        Display all the nodes values in a list
    """
    def __init__(self) -> None:
        self.top = None

    def push(self, val):
        """Add to top of our stack. If our stack is currently empty
        we set the top equal to our new node. If our stack is not empty
        we set our new node to point to our top and our new node is set
        to equal our new top.

        Parameters
        ----------
        val : int
            The value of a item.

        Returns
        -------
        None
        """
        new_node = Node(val)
        if self.top == None:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node
        return

    def pop(self):
        """Remove the top node of our stack. Set our top to the current tops
        next node.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.top = self.top.next
        return

    def peek(self):
        """Return the current top node of our stack.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        return self.top

    def is_empty(self):
        """A function to check if our stack is empty. We check if we have a top 
        node. If we dont then its empty and we return a bool.

        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if our stack is empty. False if it is not.
        """
        if self.top:
            return False
        return True

    def display(self):
        """Function to return a list containing all the values of the 
        nodes in our stack.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of all the nodes values in our stack
        """
        items = []
        current = self.top
        while current:
            items.append(current.val)
            current = current.next
        return items

print('Node Implementation')
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
print(f'Top: {stack.peek().val}')
stack.pop()
print(f'Top: {stack.peek().val}')
print(f'Items in stack (left=top, right=bottom): {stack.display()}')
print()
print()



class StackList:
    """
    A class used to represent a stack with a list.

    Attributes
    ----------
    stack : list
        A list representing a stack.

    Methods
    -------
    push(self, data)
        Insert node at the top of our stack
    pop(self, data, current_node)
        Remove the top node from the stack
    peek(self)
        Return the top of the stack.
    is_empty(self)
        Check if the stack is empty.
    display(self)
        Display all the nodes values in a list
    """
    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        """Add to top of our stack. We append to `self.stack` which is a list.

        Parameters
        ----------
        val : int
            The value of a item.

        Returns
        -------
        None
        """
        self.stack.append(val)


    def pop(self):
        """Remove the top item from stack. We pop the last element of our
        stack list.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.is_empty() != False:
            return self.is_empty()
        self.stack.pop()

    def peek(self):
        """Return the item at the top of our stack

        Parameters
        ----------
        None

        Returns
        -------
        int
            The last element in our stack list
        """
        if self.is_empty() != False:
            return self.is_empty()
        return self.stack[-1]

    def is_empty(self):
        """A function to check if our stack is empty. We check if our list is empty
        or not. We return a bool if our stack list empty or not.

        Parameters
        ----------
        None

        Returns
        -------
        bool
            True if our list is empty. False if it is not.
        """
        if self.stack:
            return False
        return f'Empty Stack'

    def display(self):
        """Function to our stack list.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of all the values in our stack
        """
        return self.stack

print('List Implementation')
stack_list = StackList()

print(f'Top: {stack_list.pop()}')
print(f'Top: {stack_list.peek()}')

stack_list.push(0)
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)
stack_list.push(4)
stack_list.push(5)
stack_list.push(6)
stack_list.push(7)

print(f'Top: {stack_list.peek()}')
stack_list.pop()
print(f'Top: {stack_list.peek()}')
stack_list.pop()
print()
print(stack_list.display())


    