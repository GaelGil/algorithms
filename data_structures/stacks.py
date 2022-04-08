class Node:
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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    """
    A class used to represent an stack

    ...

    Attributes
    ----------
    top : node
        The node at the top of the stack (set to None by default)

    Methods
    -------
    push(val)
        Adds to stop of stack
    """
    def __init__(self) -> None:
        self.top = None

    def push(self, val):
        """
        """
        new_node = Node(val)
        if self.top == None:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node
        return

    def pop(self):
        """
        """
        self.top = self.top.next
        return

    def get_top(self):
        """
        """
        return self.top

    def is_empty(self):
        if self.top == None:
            return True
        return False

    def display(self):
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


    