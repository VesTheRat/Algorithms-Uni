#Klasy
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1

class AVL:
    def __init__(self, arr):
        arr = self.quicksort(arr)
        self.node = self.avl(arr)

    def getHeight(node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
   
   def rightRotate(self, y):
       x = y.left
       T2 = x.right
       x.right = y
       y.left = T2
       y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
       x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
       return x

   def leftRotate(self, x):
       y = x.right
       T2 = y.left
       y.left = x
       x.right = T2
       x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
       y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))


   def insert(self, node, data):
       if not node:
           return self.Node(data)
       if data > node.data:
           node.right = self.insert(node.left, data)
       elif data > node.data:
           node.right = insert(node.right, data)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and self.getBalance(node.right) <= 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

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

class HMIN():
    def __init__(self, data):
        self.heap = data
        self.build_heap()

    def heapify(self, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(n, smallest)

    def build_heap(self):
        n = len(self.heap)
        for i in range(n//2-1, -1, -1):
            self.heapify(n, i)

