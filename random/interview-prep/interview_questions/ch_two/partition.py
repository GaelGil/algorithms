from node import List, Node

def partition(list, head, index=4):
    graeter_than = List()
    less_than = List()
    x =list.get(index)
    current = head
    while current.next != None:
        current = current.next
        if current.val > x:
            graeter_than.add_to_tail(current.val)
        if current.val < x:
            less_than.add_to_tail(current.val)

    print(graeter_than.display())
    print(less_than.display())
    return 0

linked_list = List()
linked_list.add_to_tail(3)
linked_list.add_to_tail(5)
linked_list.add_to_tail(8)
linked_list.add_to_tail(5)
linked_list.add_to_tail(10)
linked_list.add_to_tail(2)
linked_list.add_to_tail(1)

partition(linked_list, linked_list.head, 5)

