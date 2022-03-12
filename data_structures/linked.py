class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        pass

    def add_to_tail(self, data:int) -> None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        return

    def display(self):
        items = []
        current = self.head
        while current:
            items.append(current.val)
            current = current.next
        return items

    def length(self):
        counter = 0
        current = self.head
        while current:
            counter +=1
            current = current.next
        return counter


    def delete(self, index):
        if self.length() == 0 or self.length() <= index:
            return f'Empty List'
        # current = self.head
        # prev = self.head
        # current_index = 0
        # while current.next != None:
        #     if current_index == index:
        #         prev.next = current.next
        #         return
        #     prev = current
        #     current_index +=1
        #     current = current.next
        # return

        current = self.head.next
        prev = self.head
        counter = 0
        while current:
            if counter == index:
                prev.next = current.next
            counter += 1
            prev = current
            current = current.next

            


list = LinkedList()
list.add_to_tail(4)
list.add_to_tail(5)
list.add_to_tail(6)
list.add_to_tail(7)

print(list.display())

print(list.length())

list.delete(0)

print(list.display())
