class Node:
    def __init__(self, val=0, left=None, right=None)-> None:
        self.val = val
        self.left = None
        self.right = None
        pass


class Tree:
    def __init__(self) -> None:
        self.root = None
        pass

    def display(self):
        if self.root != None:
            self._display(self.root)
        else:
            return f'Empty Tree'
        return

    def _display(self, node):
        if node != None:
            self._display(node.left)
            print(node.val)
            self._display(node.right)
        return


    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        return

    def _insert(self, data, current_node):
        if data < current_node.val:
            if current_node.left == None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        if data > current_node.val:
            if current_node.right == None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        return 0

    def delete(self, data):            
        return


tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(18)
tree.insert(3)
tree.insert(4)
tree.insert(8)
tree.insert(16)
tree.insert(23)



tree.display()

