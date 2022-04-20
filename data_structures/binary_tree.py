from tree_node import Node

class Tree:
    """
    A class used to represent a binary tree.

    Attributes
    ----------
    root : node
        A node at the root of the tree

    Methods
    -------
    insert(self, data)
        Insert node into the three
    _insert(self, data, current_node)
        Find the correct spot to insert our node in the tree.
    get_root(self)
        return the root of out tree.
    includes(self, value)
    _sum(self)
        Get the sum of the tree.
    _min(self)
        Get the min value of our tree.
    _max(self)
        Get the max value of our tree.
    in_order(self)
        Start in order traversal.
    _in_order(self, node)
        Continue in order traversal.
    pre_order(self)
        Start pre oder traversal.
    _pre_order(self, node)
        Continue pre order traversal.
    post_order(self)
        Start post order traversal.
    _post_order(self, node)
        Continue post order_traversal.
    bfs(self)
        Preform breadth first search.
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        """Insert a node at the root if the root is empty. If its not empty
        pass node to `_insert()` to find where to properly insert the node.

        Parameters
        ----------
        data : int
            The value of a node.

        Returns
        -------
        None
        """
        if not self.root:
            new_node = Node(data)
            self.root = new_node
            return
        self._insert(data, self.root)


    def _insert(self, data, current_node):
        """Function to find where to insert a node in a binary tree.
        We check if the value we are trying to insert is greater than
        the current node. Depending on that we check the left or right
        node if they exists. We continue this proccess recursively

        Parameters
        ----------
        data : int
            The value of the node.
        current_node : node
            The node we are comparing to figure out where to add our node.

        Returns
        -------
        None
        """

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
        """Getter method for the root

        Parameters
        ----------
        None

        Returns
        -------
        node
            The root node of our binary tree
        """

        return self.root

    def includes(self, value):
        """Function to check if our binary tree includes a certain value

        Parameters
        ----------
        value : int
            The value we are tring to find in our tree.

        Returns
        -------
        bool
            True if the value we are trying to find is in our tree and false
            if it is not.
        """
        queue = [self.root]
        while queue:
            node = queue.pop()
            if node.val == value:
                return True
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return False

    def _sum(self):
        """Get the sum of our binary tree. We do this by performing bredth
        first search. 

        Parameters
        ----------
        None

        Returns
        -------
        int
            The sum of our tree.
        """
        queue = [self.root]
        sum_tree = 0
        while queue:
            node = queue.pop()
            sum_tree += node.val
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return sum_tree

    def _min(self):
        """Gets the smalest number in our tree. We do this by performing
        bredth first search.

        Parameters
        ----------
        None

        Returns
        -------
        int
            The smallest value in our binary tree.
        """
        queue = [self.root]
        min_val = self.root.val
        while queue:
            node = queue.pop()
            if node.val <= min_val:
                min_val = node.val
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return min_val

    def _max(self):
        """Get the largest value in our tree. We do this by performing breadth
        first search.

        Parameters
        ----------
        None

        Returns
        -------
        int
            The largest value in our tree.
        """
        queue = [self.root]
        max_val = self.root.val
        while queue:
            node = queue.pop()
            if node.val >= max_val:
                max_val = node.val
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return max_val

    def in_order(self):
        """Function to preform in order traversal on our binary tree.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.root:
            self._in_order(self.root) 
        return 

    def _in_order(self, node):
        """Function to continue in order traversal on our binary tree
        recursively.

        Parameters
        ----------
        node : node
            The current node to traverse

        Returns
        -------
        None
        """
        if node:
            self._in_order(node.left)
            print(node.val)
            self._in_order(node.right)
        return

    def pre_order(self):
        """Function to start pre order traversal on our binary tree. This is like depth
        first search because we explore all of a current nodes paths and nodes first
        before we explore everything else.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.root:
            self._pre_order(self.root)
        return

    def _pre_order(self, node):
        """Function to continue pre order traversal on our binary tree. 

        Parameters
        ----------
        node : node
            The node we are currently at in our traversal

        Returns
        -------
        None
        """
        if node:
            print(node.val)
            self._pre_order(node.left)
            self._pre_order(node.right)
        return

    def post_order(self):
        """Function to start post order traversal.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.root:
            self._post_order(self.root)
        return

    def _post_order(self, node):
        """Function to continue post order traversal

        Parameters
        ----------
        node : node
            The node we are currently at in our post order traversal.

        Returns
        -------
        None
        """
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.val)
        return

    def bfs(self):
        """Function to perform breadths first search

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        queue = [self.root]
        while queue:
            node = queue.pop()
            print(node.val)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
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

print()
tree.bfs()

sum_ = tree._sum()
print(f'Sum: {sum_}')

max_val = tree._max()
min_val = tree._min()

print(f'Max: {max_val}')
print(f'Min: {min_val}')