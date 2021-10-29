class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, d):
        self.head = Node(d)
        self.tail = Node()
    
    def enqueue(self, d):
        """
        This function will add to the end of the queue
        """
        new_node = Node(d)
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head == None:
            self.head = new_node

        return 
        

    def dequeue(self):
        """
        This function will remove from front of the queue
        """
        data = self.head.val
        self.head = self.head.next
        if self.head == None:
            self.tail == None
        return data

    def is_empty(self):
        return self.head == None

    def peek(self):
        if self.is_empty():
            return f'is empty'
        return self.head.val



queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.peek())
queue.dequeue()
print(queue.peek())

