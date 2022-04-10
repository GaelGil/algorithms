from logging.config import valid_ident
from msilib.schema import Class
from tkinter.messagebox import NO


class DoublyLinkedNode:
    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList(val=None, prev=self.head, next=None)
        self.size = 0

    def append(self):
        return

    def insert(self):
        return 

    def delete(self):
        return

    def get_index(self, index):
        return

    def get_value(self, val):
        return

    def get_size(self):
        return self.size