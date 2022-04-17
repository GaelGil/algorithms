class DoublyLinkedNode:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode(val=None, prev=self.head, next=None)
        self.size = 0

    def append(self):

        return

    def append_front(self):
        return

    def insert_after_value(self, value):
        return

    def insert_at_index(self, index):
        return 

    def delete(self):
        return

    def get_index(self, index):
        return

    def get_value(self, val):
        return

    def get_size(self):
        return self.size