class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, data):
        return 

    def dequeue(self):

        return

    def get_lenght(self):
        return


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