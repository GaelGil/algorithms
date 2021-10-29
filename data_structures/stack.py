class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = Node()
    
    def add_to_top(self, d):
        """
        This function will add to the top of a stack. 
        """
        new_node = Node(d)
        self.top.next = new_node
        new_node.next = self.top
        self.top = new_node
        return 0
        

    def remove_top(self):
        """
        This function will remove from the top. 
        """
        print(self.top.next.val)
        
        return 0

    def peek(self):
        return self.top.val


stack = Stack()
stack.add_to_top(1)
stack.add_to_top(2)
stack.add_to_top(3)
print(stack.peek())

stack.remove_top()


