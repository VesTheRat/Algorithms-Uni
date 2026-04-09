import random

### KLASY ###

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.node = None

    def insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.data:
            current_node.left = self.insert(current_node.left, value)
        elif value > current_node.data:
            current_node.right = self.insert(current_node.right, value)
        return current_node

    def build_bst_fcfs(self, elements):
        if not elements:
            return
        for value in elements:
            self.node = self.insert(self.node, value)

    def print_inOrderTraverse(self, node):
        if node is not None:
            self.print_inOrderTraverse(node.left)
            print(node.data)
            self.print_inOrderTraverse(node.right)

    def find_min_path(self):
        path = []
        current = self.node
        if current is None:
            return None, []
        
        while current:
            path.append(current.data)
            if current.left is None:
                break
            current = current.left
        return current.data, path
    
    def find_max_path(self):
        path = []
        current = self.node
        if current is None:
            return None, []
        
        while current:
            path.append(current.data)
            if current.right is None:
                break
            current = current.right
        return current.data, path
    
dane = random.sample(range(0, 100), 15)


### PROGRAM ###

tree = BST()
tree.build_bst_fcfs(dane)

minVal, minPath = tree.find_min_path()
maxVal, maxPath = tree.find_max_path()

print(f"Dane: {dane}")
tree.print_inOrderTraverse(tree.node)
print(f"Min: {minVal}, path: {minPath}")
print(f"Max: {maxVal}, path: {maxPath}")
