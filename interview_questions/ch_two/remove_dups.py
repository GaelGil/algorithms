from typing import Counter
from node import List, Node

def remove_dupes(list, head):
    """
    Function to remove duplicates from a list
    This function will go through all the elemnts in a linked list
    we will add all the elements to a dictionary as we go. We will
    then check the dictionary if it we have seen that value before
    if so then it is a duplicate and we will delete the node.
    """
    seen = {}
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

# print(linked_list.get(3))
# print()
remove_dupes(linked_list, linked_list.head)


# print(linked_list.display())
# print()
# print(linked_list.delete(6))
print(linked_list.display())
