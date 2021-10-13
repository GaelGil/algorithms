# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Input: head = [1,2]
# Output: [2,1]
#        0 <- 1 <- 2 <- 3 <- 4 
#                            ^s   ^f    ^next

def reverseList(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    prevNode = None 
    currentNode = head
    
    while currentNode is not None:
        tempNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = tempNode
    
    return prevNode
    




newList = ListNode(1, 2)
reverseList(newList)
