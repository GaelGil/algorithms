


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def Node(self, num) -> Node:
        self.data = num

    def append_to_tail(self, num):
        end = Node(num)
        self.
        while(n.next != None):
            n = n.next
        n.next = end

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        node = Node(data, self.head)
        self.