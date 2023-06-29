class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class List:
    def __init__(self):
       self.head = Node()

    def add_to_tail(self, d):
        new_node = Node(d)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        return 0

    def delete(self, index):
        if self.length() == 0:
            return f'nothing in list'
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

    def length(self):
        total = 0
        if self.head == None:
            return 'nothing in list'
        current = self.head
        while current.next != None:
            total +=1
            current = current.next
        return total

    def get(self, index):
        current = self.head
        counter = 0
        while current.next != None:
            current = current.next
            if counter == index:
                return current.val
            counter += 1
        return f'nothing at index: {index}' 

    def display(self):
        elements = []
        if self.head == None:
            return 'nothing in list'
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.val)
        return elements
    