import random

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(node, value):
    if node is None:
        return Node(value)
    if value == node.data:
        return
    elif value < node.data:
        node.left = insert(node.left, value)
    else:
        if value > node.data:
            node.right = insert(node.right, value)
    return node

def build_bst_fcfs(elements):
    if not elements:
        return None
    root = Node(elements[0])

    for i in range(1, len(elements)):
        insert(root, elements[i])

    return root

def print_inOrderTraverse(node):
    if node is not None:
        print_inOrderTraverse(node.left)
        print(node.data)
        print_inOrderTraverse(node.right)

