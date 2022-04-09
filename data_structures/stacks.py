from node import Node


class Stack:
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
        """Insert a node at the root if the root is empty. If its not empty
        pass node to `_insert()` to find where to properly insert the node.

        Parameters
        ----------
        data : int
            The value of a node.

        Returns
        -------
        None
        """
        self.top = self.top.next
        return

    def get_top(self):
        """Insert a node at the root if the root is empty. If its not empty
        pass node to `_insert()` to find where to properly insert the node.

        Parameters
        ----------
        data : int
            The value of a node.

        Returns
        -------
        None
        """
        return self.top

    def is_empty(self):
        """Insert a node at the root if the root is empty. If its not empty
        pass node to `_insert()` to find where to properly insert the node.

        Parameters
        ----------
        data : int
            The value of a node.

        Returns
        -------
        None
        """
        if self.top:
            return False
        return True

    def display(self):
        """Insert a node at the root if the root is empty. If its not empty
        pass node to `_insert()` to find where to properly insert the node.

        Parameters
        ----------
        data : int
            The value of a node.

        Returns
        -------
        None
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
print(f'Top: {stack.get_top().val}')
stack.pop()
print(f'Top: {stack.get_top().val}')
print(f'Items in stack (left=top, right=bottom): {stack.display()}')
print()
print()



class StackList:
    """
    A class used to represent a stack with nodes

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
    get_top(self)
        Return the top of the stack.
    is_empty(self)
        Check if the stack is empty.
    display(self)
        Get the sum of the tree.
    """
    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty() != False:
            return self.is_empty()
        self.stack.pop()

    def get_top(self):
        if self.is_empty() != False:
            return self.is_empty()
        return self.stack[-1]

    def is_empty(self):
        if self.stack:
            return False
        return f'Empty Stack'

    def display(self):
        items = []
        if self.is_empty() != False:
            return self.is_empty()
        for i in range(len(self.stack), 0, -1):
            items.append(self.stack[-i])
        return items

print('List Implementation')
stack_list = StackList()

print(f'Top: {stack_list.pop()}')
print(f'Top: {stack_list.get_top()}')

stack_list.push(0)
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)
stack_list.push(4)
stack_list.push(5)
stack_list.push(6)
stack_list.push(7)

print(f'Top: {stack_list.get_top()}')
stack_list.pop()
print(f'Top: {stack_list.get_top()}')
stack_list.pop()
print()
print(stack_list.display())


    