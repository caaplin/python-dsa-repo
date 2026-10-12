class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")

tree = BinaryTree(root)

print("Inorder traversal:")
tree.inorder(tree.root)
print()

print("Preorder traversal:")
tree.preorder(tree.root)
print()

print("Postorder traversal:")
tree.postorder(tree.root)
print()

# Performance comparison:
# Each traversal visits every node once, so all three take O(n) time.
# Recursive traversal uses O(h) extra stack space, where h is the tree height.
# In a balanced tree, h is O(log n); in a skewed tree, h is O(n).

