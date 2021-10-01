

from binarytree import tree, bst, Node, build

class MyNode:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)

b = bst(height=5, is_perfect=True)
print(b)

