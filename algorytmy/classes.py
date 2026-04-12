#Klasy
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class AVL:
    def __init__(self,arr):
        arr = self.quicksort(arr)
        self.node = self.avl(arr)
    
    def avl(self,arr):
        if not arr:
            return None
        middle_index = len(arr) // 2
        node = Node(arr[middle_index])

        node.left = self.avl(arr[:middle_index])
        node.right = self.avl(arr[middle_index + 1:])
        return node

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)

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
            self.heap[i], self.heap[smallest] = self.heap[smallest]
            self.heapify(n, smallest)

    def build_heap(self):
        n = len(self.heap)
        for i in range(n//2-1, -1, -1):
            self.heapify(n, i)


