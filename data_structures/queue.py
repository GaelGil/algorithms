class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, d):
        new_node = Node(d)
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head == None:
            self.head = new_node
        return 0

    def dequeue(self):
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return 0

    def is_empty(self):
        return self.head == None

    def peek(self):
        return self.head.val
    def get_tail(self):
        return self.tail.val

    def display(self) -> list:
        queue = []
        current = self.head
        while current.next != None:
            queue.append(current)
            current = current.next
        return queue



queue = Queue()
queue.enqueue(1)
print(queue.get_tail())
queue.enqueue(2)
print(queue.get_tail())


queue.enqueue(3)
print(queue.get_tail())

queue.enqueue(4)
print(queue.get_tail())
print(queue.peek())
print()

queue.dequeue()
queue.dequeue()


print(queue.peek())
print(queue.get_tail())



