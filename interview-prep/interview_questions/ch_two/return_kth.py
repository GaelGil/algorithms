from node import List, Node

def return_kth_last(head, kth=3):
    current = head
    while current.next != None:
        current = current.next
        if current.val == 3:
            return f'found: {current.val}'
    return 0


linked_list = List()

linked_list.add_to_tail(1)
linked_list.add_to_tail(2)
linked_list.add_to_tail(3)
linked_list.add_to_tail(4)
linked_list.add_to_tail(4)
linked_list.add_to_tail(4)
linked_list.add_to_tail(5)
linked_list.add_to_tail(6)
linked_list.add_to_tail(7)
linked_list.add_to_tail(8)
linked_list.add_to_tail(9)
linked_list.add_to_tail(9)
linked_list.add_to_tail(10)


print(return_kth_last(linked_list.head))