class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
       self.head = Node()

    def add_to_tail(self, d):
        """
        This function will add a new node to the end of our linked list.
        We do this by looping through the whole list. Once we get to the
        end of the list our `current` node will be the node that is at
        the end. This takes O(N) time
        """
        new_node = Node(d)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        return 0

    def length(self):
        """
        This function will count all our elements in our linked list
        (not includin head). We loop through the whole list and we add
        to a counter `total`. Then at the end we return our `total`
        """
        current = self.head
        total = 0
        while current.next != None:
            current = current.next
            total +=1
        return total

    def display(self):
        """
        This function will display all the elements in our list. 
        """
        current = self.head
        elements = []
        while current.next != None:
            current = current.next
            elements.append(current.val)
        return elements


    def delete(self, index):
        """
        This function will delete a element in our linked list given a
        index. If the index is greter then the length of the list we 
        return a message. If not we continue. We set a var `current`
        equal to head and create a `current_index` at 0. We start to
        loop through the list and create a `prev_node`. This node will
        be the node before the `current`. Right after we do that we set
        `curent` euqal to `current.next` as we move in the list. If our
        `index` is equal to our `current_index`. We select the `prev_node.next`
        and set that equal the the `current.next`. Here is an example

        [1, 1, 2, 1, 1]
        prev: 0
        current: 1

        prev: 1
        current: 1

        prev: 1
        current: 2

        prev.next: 2
        current.next: 1
        [1, 1, 1, 1]

        This takes O(N) time
        """
        if index > self.length():
            return f'index {index} is out of range'

        current = self.head
        current_index = 0
        while True:
            prev_node = current
            current = current.next
            print(f'prev: {prev_node.val}')
            print(f'current: {current.val}')
            print()
            if current_index == index:
                print(f'prev.next: {prev_node.next.val}')
                print(f'current.next: {current.next.val}')
                prev_node.next = current.next
                return
            current_index += 1



list = LinkedList()
list.add_to_tail(1)
list.add_to_tail(1)
list.add_to_tail(2)
list.add_to_tail(1)
list.add_to_tail(1)

print(list.display())
# print(list.length())
list.delete(2)
print(list.display())
