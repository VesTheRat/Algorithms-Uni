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

def find_min_path(root):
    path = []
    current = root
    if current is None:
        return None, []

    while current:
        path.append(current.data)
        if current.left is None:
            break
        current = current.left
    return current.data, path

def find_max_path(root):
    path = []
    current = root
    if current is None:
        return None, []

    while current:
        path.append(current.data)
        if current.right is None:
            break
        current = current.right
    return current.data, path

def find_level(node, key, level=0):
    if node is None:
        return None
    if node.data == key:
        return level
    if key < node.data:
        return find_level(node.left, key, level + 1)
    else:
        return find_level(node.right, key, level +1)

def find_node(node,key):
    if node is None or node.data == key:
        return node
    if key < node.data:
        return find_node(node.left, key)
    return find_node(node.right, key)

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

def remove_from_parent(node,key):
    if node is None: return None
    if node.data == key:
        delete_subtree(node)
        return None
    if key < node.data:
        node.left = remove_from_parent(node.left, key)
    else:
        node.right = remove_from_parent(node.right, key)
    return node

def collect_level(node, target_level, current_level, list_out):
    if node is None:
        return
    if current_level == target_level:
        list_out.append(node.data)
        return
    collect_level(node.left, target_level, current_level + 1, list_out)
    collect_level(node.right, target_level, current_level + 1, list_out)

def print_tree(node,level=0):
    if node is not None:
        print_tree(node.right, level+1)
        print(" "*level+str(node.data))
        print_tree(node.left, level+1)

# Quicksort do AVL
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quicksort(left)+[pivot]+quicksort(right)
