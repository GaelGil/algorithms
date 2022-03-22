from platform import node
import re


class Node:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            new_node = Node(data)
            self.root = new_node
            return
        self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.val:
            if not current_node.left:
                current_node.left = Node(data)
                return
            else:
                self._insert(data, current_node.left)
                return
        if data >= current_node.val:
            if not current_node.right:
                current_node.right = Node(data)
                return
            else:
                self.insert(data, current_node.right)
        return

    def get_root(self):
        return self.root


    # def display:



tree = Tree()
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(5)
tree.insert(12)

print(tree.get_root().val)
print(tree.root.left.val)
print(tree.root.left.left.val)

print(tree.root.right.val)
# print(tree.root.right.right.val)

