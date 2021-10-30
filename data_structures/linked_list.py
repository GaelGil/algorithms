class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
       self.head = None

    def add_to_tail(self, d):
        """
        This function will add a new node to the end of our linked list.
        We do this by looping through the whole list. Once we get to the
        end of the list our `current` node will be the node that is at
        the end. This takes O(N) time
        """
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        return

    def length(self):
        """
        This function will count all our elements in our linked list
        (not includin head). We loop through the whole list and we add
        to a counter `total`. Then at the end we return our `total`
        """
        if self.head == None:
            return f'Empty List'
        # start at one for head (we can do this because we know head is not None)
        counter = 1 
        current = self.head
        while current.next != None:
            current = current.next
            counter +=1
        return counter

    def display(self):
        """
        This function will display all the elements in our list. 
        """
        if self.head == None:
            return f'Empty List'
        current = self.head
        elements = []
        elements.append(current.val)
        while current.next != None:
            current = current.next
            elements.append(current.val)
        return elements

    def delete(self, index):
        """
        This function will delete a node given an index
        """
        if self.length() == 0:
            return f'Empty List'
        if index == 0:
            self.head = self.head.next
        current_index = 0
        # keep track of the previos node
        prev = self.head
        current = self.head
        while current.next != None:
            if current_index == index:
                prev.next = current.next
                return
            prev = current
            current_index +=1
            current = current.next
        return

list = LinkedList()
# print(list.display())
list.add_to_tail(1)
list.add_to_tail(1)
list.add_to_tail(2)
list.add_to_tail(1)
list.add_to_tail(1)
print(list.display())
print(list.length())
# list.delete(0)
print(list.display())
