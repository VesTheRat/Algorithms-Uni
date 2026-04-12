### FUNKCJE ###
def print_inOrderTraverse(node):
    if node is not None:
        print_inOrderTraverse(node.left)
        print(node.data, end=" ")
        print_inOrderTraverse(node.right)

def print_reverseTraverse(node):
    if node is not None:
        print_reverseTraverse(node.right)
        print(node.data, end=" ")
        print_reverseTraverse(node.left)

def inorder_list(node, elements):
    if node:
        inorder_list(node.left, elements)
        elements.append(node.data)
        inorder_list(node.right, elements)

def find_min_path(node):
    path = []
    if node is None:
        return None, []
    while node:
        path.append(node.data)
        if node.left is None:
            break
        node = node.left
    return node.data, path

def find_max_path(node):
    path = []
    if node is None:
        return None, []
    while node:
        path.append(node.data)
        if node.right is None:
            break
        node = node.right
    return node.data, path

def find_level(node, data, level=0):
    if node is None:
        return None
    if node.data == data:
        return level
    if data < node.data:
        return find_level(node.left, data, level + 1)
    else:
        return find_level(node.right, data, level +1)

def find_node(node, data):
    if node is None or node.data == data:
        return node
    if data < node.data:
        return find_node(node.left, data)
    return find_node(node.right, data)

def get_height(node):
    if node is None:
        return 0
    return 1 + max(get_height(node.left),get_height(node.right))

def delete_subtree(node):
    if node:
        delete_subtree(node.left)
        delete_subtree(node.right)
        node.left = None
        node.right = None

def remove_from_parent(node, data):
    if node is None: 
        return None
    if node.data == data:
        delete_subtree(node)
        return None
    if data < node.data:
        node.left = remove_from_parent(node.left, data)
    else:
        node.right = remove_from_parent(node.right, data)
    return node

def collect_level(node, target_level, current_level, list_out):
    if node is None:
        return
    if current_level == target_level:
        list_out.append(node.data)
        return
    collect_level(node.left, target_level, current_level + 1, list_out)
    collect_level(node.right, target_level, current_level + 1, list_out)

def balanced_bst(elements):
    if not elements:
        return None
    mid = len(elements)//2
    node = Node(elements[mid])
    node.left = balanced_bst(elements[:mid])
    node.right = balanced_bst(elements[mid+1:])
    return node

def balance_by_root_extraction(root):
    elements = []
    inorder_list(root, elements)
    return balanced_bst(elements)

#Funkcje hmin
def get_path_hmin(heap, index):
    path = []
    while index >= 0:
        path.append(heap.heap[index])
        if index == 0: 
            break
        index = (index -1)//2
    return path[::-1]

def find_min_hmin(heap):
    if not heap.heap: 
        return None
    return heap.heap[0], heap.get_path(0)

def find_max_hmin(heap):
    if not heap.heap:
        return None
    n = len(heap.heap)
    start = n//2
    max_v = heap.heap[start]
    max_i = start
    for i in range(start + 1, n):
        if heap.heap[i] > max_v:
            max_v = heap.heap[i]
            max_i = i
    return max_v, heap.get_path(max_i)

###

def find_level_hmin(heap, key):
    idx = -1
    for i in range(len(heap)):
        if heap[i] == key:
            idx = i
            break
    if idx == -1:
        print("Brak klucza")
    level = (idx + 1).bit_length() - 1
    start_idx = 2**level - 1
    end_idx = 2**(level + 1) - 1
    elements_on_level = heap[start_idx : min(end_idx, len(heap))]
    return level, elements_on_level

###

def descending(heap):
    temp_heap = list(heap)
    n = len(temp_heap)
    sorted_elements = []
    for i in range(n):
        sorted_elements.append(temp_heap[0])
        temp_heap[0] = temp_heap[len(temp_heap)-1]
        temp_heap.pop()
        if temp_heap:
            temp_heap.heapify(len(temp_heap), 0)
    return sorted_element[::-1]

###

def get_children(i):
    left = 2*i+1
    right = 2*i+2
    lista = []
    if left < len(heap): lista.append(left)
    if right < len(heap): lista.appned(right)
    return lista

def pre_order(i):
    x = [heap[i]]
    for child in get_children(i):
        x.extend(pre_order(child))
    return res

def get_height(i):
    children = get_children(i)
    if not children:
        return 0
    return 1 + max(get_height(c) for c in children)

def post_order_indices(i):
    indices = []
    for child in get_children(i):
        indices.extend(post_order_indices(child))
    indices.append(i)
    return indices

def get_heap_substructure(heap, key):
    root = -1
    for i in range(len(heap)):
        if heap[i] == key:
            root = i
            break
    if root == -1:
        print("Brak klucza")
        return
    poddrzewo = pre_order(root)
    wysokość = get_height(root)
    remove = post_order_indices(root)
    heap = [heap[i] for i in remove]
    for i in sorted(remove, reverse=True):
        heap.pop[i]
    after_removal = heap
    return poddrzewo, height, after_removal

    ###
