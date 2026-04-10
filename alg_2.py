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

    def insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(node.right, data)

    def build_bst_fcfs(self, elements):
        if not elements:
            return
        for value in elements:
            self.node = self.insert(self.node, value)

    def print_inOrderTraverse(self, node):
        if node is not None:
            self.print_inOrderTraverse(node.left)
            print(node.data, end=" ")
            self.print_inOrderTraverse(node.right)

    def print_reverseTraverse(self, node):
        if node is not None:
            self.print_reverseTraverse(node.right)
            print(node.data, end=" ")
            self.print_reverseTraverse(node.left)

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

    def find_level(self, current_node, key, level=0):
        if current_node is None:
            return None
        if current_node.data == key:
            return level
        if key < current_node.data:
            return self.find_level(current_node.left, key, level + 1)
        else:
            return self.find_level(current_node.right, key, level +1)

    def find_node(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.find_node(node.left, data)
        return self.find_node(node.right, data)

    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def delete_subtree(self, node):
        if node:
            self.delete_subtree(node.left)
            self.delete_subtree(node.right)
            node.left = None
            node.right = None

    def remove_from_parent(self, node, data):
        if node is None: return None
        if node.data == data:
            self.delete_subtree(node)
            return None
        if data < node.data:
            node.left = self.remove_from_parent(node.left, data)
        else:
            node.right = self.remove_from_parent(node.right, data)
        return node 

    def collect_level(self, current_node, target_level, current_level, list_out):
        if current_node is None:
            return
        if current_level == target_level:
            list_out.append(current_node.data)
            return
        self.collect_level(current_node.left, target_level, current_level + 1, list_out)
        self.collect_level(current_node.right, target_level, current_level + 1, list_out)

### PROGRAM ###
dane = random.sample(range(0, 100), 15)
tree = BST()
tree.build_bst_fcfs(dane)

minVal, minPath = tree.find_min_path()
maxVal, maxPath = tree.find_max_path()

wartosci = [] #lista wartosci na tym samym poziomie co klucz
klucz = random.choice(dane)
poziom = tree.find_level(tree.node, klucz)
if poziom is not None:
    tree.collect_level(tree.node, poziom, 0, wartosci)


print(f"Dane: {dane}")
tree.print_inOrderTraverse(tree.node)
print()
tree.print_reverseTraverse(tree.node)
print()
print(f"Min: {minVal}, path: {minPath}")
print(f"Max: {maxVal}, path: {maxPath}") 
if poziom is not None:
    print(f"Klucz: {klucz}, poziom: {poziom}, pozostałe elementy: {wartosci}")
else:
    print(f"Brak klucza w BST")
wezel = tree.find_node(tree.node, klucz)
if wezel is not None:
    tree.print_inOrderTraverse(wezel)
    print(f"Wysokość poddrzewa: {tree.get_height(wezel)}")
    tree.node = tree.remove_from_parent(tree.node, klucz)
    print(f"Elementy pozostałe w drzewie:")
    tree.print_inOrderTraverse(tree.node)
else:
    print("Brak klucza w BST")
