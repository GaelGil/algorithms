

class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head.val == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def add_infront(self, data) -> None:
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def display(self) -> list:
        items = []
        current = self.head
        while current:
            items.append(f'{current.val} ->')
            current = current.next
        return items

    def get_head(self):
        return self.head


    def get_last(self):
        current = self.head
        while current.next != None:
            current = current.next
        return current


    def get_item(self, item):
        return

    def delete(self, item):
        return


list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print(list.display())


# print(list.get_head().val)


list.add_infront(0)
print(list.display())


print(list.get_last().val)