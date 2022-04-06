class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
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
                self._insert(data, current_node.right)
        return

    def get_root(self):
        return self.root

    def find(self):
        return

    def in_order(self):
        if self.root:
            self._in_order(self.root) 
        return 

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.val)
            self._in_order(node.right)
        return

    def pre_order(self):
        """ like depth first search (explore all the nodes and their paths then go back) 
        """
        if self.root:
            self._pre_order(self.root)
        return

    def _pre_order(self, node):
        if node:
            print(node.val)
            self._pre_order(node.left)
            self._pre_order(node.right)
        return

    def post_order(self):
        if self.root:
            self._post_order(self.root)
        return

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.val)
        return



tree = Tree()
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(5)
tree.insert(12)


print()
tree.in_order()

print()
tree.post_order()

print()
tree.pre_order()


# In depth first search if you have a node you must visit all the other nodes on that node until it has no connections before moving on.
# In breadth first search you check all nodes at once until you can't check anymore.

# Implement dfs and bfs in trees 