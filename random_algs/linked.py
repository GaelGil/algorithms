class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    

    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



nums_list = LinkedList()
nums_list.head = Node(1)
second = Node(2)
third = Node (3)
forth = Node(4)
fifth = Node(5)



nums_list.head.next = second
second.next = third
third.next = forth 
forth.next = fifth


nums_list.print_linked_list() 



    
