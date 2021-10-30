from typing import Counter


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def enqueue(self, d):
        node = Node(d)
        # if the tail is not empty 
        if self.tail != None:
            # set the tail.next to the new node
            self.tail.next = node
        # update the stack so that the tail is the new node
        self.tail = node
        # if the head is empty then are new node is the head
        if self.head == None:
            self.head= node
        return 0

    def dequeue(self):
        data = self.head.val
        if self.is_empty():
            return f'empty'
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return data

    def is_empty(self):
        return self.head == None

    def peek(self):
        if self.is_empty():
            return f'empty'
        return self.tail.val



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.peek())
queue.dequeue()
queue.dequeue()

# queue.dequeue()
# queue.dequeue()
# queue.dequeue()

# print(queue.peek())


# elf.head