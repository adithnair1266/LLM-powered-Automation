class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = TreeNode(value)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

# Testing
tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.print_tree(tree.root)