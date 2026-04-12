import random
from classes import BST, AVL
import funkcje as f


### PROGRAM ###
# dane = random.sample(range(0, 100), 15)
dane = [4,6,3,5,8,2,6,0,9]
tree = BST()
tree.build_bst_fcfs(dane)

minVal, minPath = f.find_min_path(tree.node)
maxVal, maxPath = f.find_max_path(tree.node)

wartosci = [] #lista wartosci na tym samym poziomie co klucz
klucz = dane[3]
poziom = f.find_level(tree.node, klucz)
if poziom is not None:
    f.collect_level(tree.node, poziom, 0, wartosci)

print(f"Dane: {dane}")
f.print_inOrderTraverse(tree.node)
print()
f.print_reverseTraverse(tree.node)
print()
print(f"Min: {minVal}, path: {minPath}")
print(f"Max: {maxVal}, path: {maxPath}")
if poziom is not None:
    print(f"Klucz: {klucz}, poziom: {poziom}, pozostałe elementy: {wartosci}")
else:
    print(f"Brak klucza w BST")
wezel = f.find_node(tree.node, klucz)
if wezel is not None:
    f.print_inOrderTraverse(wezel)
    print(f"Wysokość poddrzewa: {f.get_height(wezel)}")
    tree.node = f.remove_from_parent(tree.node, klucz)
    print(f"Elementy pozostałe w drzewie:")
    f.print_inOrderTraverse(tree.node)
else:
    print("Brak klucza w BST")
