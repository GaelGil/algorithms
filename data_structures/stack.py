class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self,d=0):
        self.top = Node(d)
    
    def add(self, d):
        """
        This function will add to the top of a stack. 
        """
        # create new node
        new_node = Node(d)
        # set new_node.next to point to old top
        new_node.next = self.top
        # update the new top
        self.top = new_node
        return 0
        

    def remove(self):
        """
        This function will remove from the top. 
        """
        self.top = self.top.next
        return 0

    def is_empty(self):
        return self.top == None

    def peek(self):
        if self.is_empty():
            return f'is empty'
        return self.top.val


# initialize with 1 at bottom
stack = Stack(1)
stack.add(2)
stack.add(3)
stack.add(4)
print(f'before removing: {stack.peek()}')

stack.remove()

print(f'after removing: {stack.peek()}')



