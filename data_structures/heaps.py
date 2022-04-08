class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Heap:
    def __init__(self) -> None:
        self.root = None

    def insert(self):
        return

    def _insert(self):
        return

    def bfs(self):
        queue = [self.root]
        while queue:
            node = queue.pop()
            print(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return

    def dfs(self):
        return