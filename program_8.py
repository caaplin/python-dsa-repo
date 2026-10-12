class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.value = successor.value
            node.right = self._delete_node(node.right, successor.value)

        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)


print("Binary search tree")
tree = BinarySearchTree()

for value in (50, 30, 70, 20, 40, 60, 80):
    tree.insert(value)

print("Inorder after insertion:")
tree.inorder(tree.root)
print()
print("Search for 40:", tree.search(40))
print("Search for 90:", tree.search(90))

tree.delete(30)
print("After deleting 30:")
tree.inorder(tree.root)
print()


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

binary_tree = BinaryTree(root)

print("Binary tree traversals")
print("Inorder:")
binary_tree.inorder(binary_tree.root)
print()
print("Preorder:")
binary_tree.preorder(binary_tree.root)
print()
print("Postorder:")
binary_tree.postorder(binary_tree.root)
print()


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = QueueNode(value)

        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        for existing in self.vertices:
            if existing == vertex:
                return
        self.vertices = self.vertices + [vertex]

    def add_edge(self, start, end):
        self.add_vertex(start)
        self.add_vertex(end)
        self.edges = self.edges + [(start, end), (end, start)]

    def has_been_visited(self, visited, vertex):
        for item in visited:
            if item == vertex:
                return True
        return False

    def bfs(self, start):
        queue = LinkedQueue()
        visited = [start]
        queue.enqueue(start)

        while not queue.is_empty():
            current = queue.dequeue()
            print(current, end=" ")

            for edge in self.edges:
                if edge[0] == current:
                    neighbor = edge[1]
                    if not self.has_been_visited(visited, neighbor):
                        visited = visited + [neighbor]
                        queue.enqueue(neighbor)

    def dfs(self, start, visited):
        visited = visited + [start]
        print(start, end=" ")

        for edge in self.edges:
            if edge[0] == start:
                neighbor = edge[1]
                if not self.has_been_visited(visited, neighbor):
                    visited = self.dfs(neighbor, visited)

        return visited


print("Graph traversals")
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")

print("BFS from A:")
graph.bfs("A")
print()
print("DFS from A:")
graph.dfs("A", [])
print()

# Performance comparison:
# BST insert, search, and delete take O(h), where h is the tree height.
# For a balanced BST, h is O(log n); for a skewed BST, h is O(n).
# Inorder, preorder, and postorder traversals each take O(n) time
# and O(h) recursive stack space.
# BFS and DFS normally take O(V + E) time with an adjacency-list graph.
# This graph scans its edge list for each visited vertex, so its traversals
# take O(V * E) time. BFS uses O(V) extra space; recursive DFS uses O(V)
# visited storage and up to O(V) call-stack space.

