class Node:
    """
    A class used to represent a single node.

    Attributes
    ----------
    val : int
        Value of the node
    next : node
        The address of the next node (set to None by default)

    Methods
    -------
    None
    """
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


def merge(head_one, head_two):
    current_one = head_one
    current_two = head_two
    root = []
    while current_one.next or current_two:
        if current_one.val > current_two.val:
            root.append(current_two.val)
            current_two = current_two.next
        elif current_two.val > current_one.val:
            root.append(current_one.val)
            current_one = current_one.next
        else:
            root.append(current_one.val)
            root.append(current_two.val)
            current_one = current_one.next
            current_two = current_two.next

    return root



root1 = Node(1)
root1.next = Node(4)
root1.next.next = Node(7)

root2 = Node(0)
root2.next = Node(3)
root2.next.next = Node(5)

# print(root1.next.val)
print(merge(root1, root2))