class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        return

    def dequeue(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        return

    def display(self):
        items = []
        current = self.head
        while current:
            items.append(current.val)
            current = current.next
        return items

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

print('Node Implementation')
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()
q.dequeue()


print(f'Display: {q.display()}')
print(f'Head: {q.get_head().val}')
print(f'tail: {q.get_tail().val}')
print()
print()



class QueueList:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        return 

    def dequeue(self):
        self.queue.pop()
        return

    def get_head(self):
        return self.queue[-1]

    def get_tail(self):
        return self.queue[0]

    def get_lenght(self):
        return len(self.queue)

    def display(self):
        return self.queue


q = QueueList()
q.enqueue(1)
q.enqueue(12)
q.enqueue(23)
q.enqueue(34)
q.enqueue(45)
q.enqueue(56)
q.enqueue(67)
q.enqueue(78)


print(f'List Implementation')
print(f'Head: {q.get_head()}')
print(f'Tail: {q.get_tail()}')
print(f'Queue: {q.display()}')
print()
q.dequeue()
q.dequeue()
q.dequeue()
print(f'Head: {q.get_head()}')
print(f'Tail: {q.get_tail()}')
print(f'Queue: {q.display()}')