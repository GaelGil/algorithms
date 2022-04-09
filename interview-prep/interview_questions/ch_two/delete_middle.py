from node import List, Node

def delete_mid(list, head):
    length = list.length()
    print(length)
    mid = int(length/2)
    current = head 
    index_counter = 0
    while current.next != None:
        current = current.next
        if index_counter == mid:
            list.delete(index_counter)
        index_counter +=1 
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

print(linked_list.display())
# linked_list.delete(2)
delete_mid(linked_list, linked_list.head)
print(linked_list.display())

