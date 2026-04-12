from classes import Node, HMIN

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
    return heap.heap[0], get_path_hmin(heap, 0)

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
    return max_v, get_path_hmin(heap, max_i)

###

def find_level_hmin(heap, key):
    idx = -1
    for i in range(len(heap.heap)):
        if heap.heap[i] == key:
            idx = i
            break
    if idx == -1:
        print("Brak klucza")
    level = (idx + 1).bit_length() - 1
    start_idx = 2**level - 1
    end_idx = 2**(level + 1) - 1
    elements_on_level = heap.heap[start_idx : min(end_idx, len(heap.heap))]
    return level, elements_on_level

###

def descending(heap):
    temp_heap = list(heap.heap)
    n = len(temp_heap)
    sorted_elements = []
    temp_hmin = HMIN(temp_heap)
    for i in range(n):
        sorted_elements.append(temp_heap[0])
        if len(temp_hmin.heap) > 1:
            temp_hmin.heap[0] = temp_hmin.heap.pop()
            temp_hmin.heapify(len(temp_hmin.heap), 0)
        else:
            temp_hmin.heap.pop()
    return sorted_elements[::-1]

###
def get_heap_substructure(heap,key):
    heap_list = heap.heap
    try:
        root_idx = heap_list.index(key)
    except ValueError:
        return None, 0, []

    def get_children_idx(i):
        left = 2*i+1
        right = 2*i+2
        res = []
        if left < len(heap_list): res.append(left)
        if right < len(heap_list): res.append(right)
        return res

    def pre_order_collect(i):
        res = [heap_list[i]]
        for child in get_children_idx(i):
            res.extend(pre_order_collect(child))
        return res
    
    def get_h(i):
        children = get_children_idx(i)
        if not children:
            return 0
        return 1 + max(get_h(c) for c in children)

    def get_all_descendant_indices(i):
        indices = [i]
        for child in get_children_idx(i):
            indices.extend(get_all_descendant_indices(child))
        return indices

    poddrzewo = pre_order_collect(root_idx)
    wysokosc = get_h(root_idx)
    indices_to_remove = sorted(get_all_descendant_indices(root_idx), reverse=True)
    new_heap = list(heap_list)
    for idx in indices_to_remove:
        new_heap.pop(idx)
    
    return poddrzewo, wysokosc, new_heap

    ###
