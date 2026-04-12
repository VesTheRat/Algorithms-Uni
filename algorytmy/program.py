from classes import BST, AVL, HMIN
import funkcje as f
import generator
import random

### PROGRAM ###
generator()

with open("listy_sorted.txt", "r+", encoding='utf-8') as f:
    tekst = f.read().split()
    
dane = [int(x) for x in tekst]

bst = BST()
avl = AVL()
hmin = HMIN(dane)

bst.built_bst_fcfs(dane)
avl.avl(dane)

print("BST: ")
f.print_inOrderTraverse(bst)
zrownowazone = f.balance_by_root_extraction(bst)
print("\nPo zrównoważeniu: ")
f.inOrderTraverse(zrownowazone

print("\nAVL: ", end="")
f.print_inOrderTraverse(avl)

print(f"\nHMIN: {*hmin}")


### MENU ###
while True:
    print("Wybierz funkcję:\n1.Min/Max\n2.Poziom względem klucza\n3.Elementy malejąco\n4.Pre-order\n5.Koniec")
    func = input(">")
    match func:
        case "1":

            minVal_bst, minPath_bst = f.find_min_path(bst_tree.node)
            maxVal_bst, maxPath_bst = f.find_max_path(bst_tree.node)

            minVal_avl, minPath_avl = f.find_min_path(avl_tree.node)
            maxVal_avl, maxPath_avl = f.find_max_path(avl_tree.node)

            minVal_hmin, minPath_hmin = f.find_min_hmin(hmin.heap)
            maxVal_hmin, maxPath_hmin = f.find_max_hmin(hmin.heap)

            print("BST: ")
            print(f"Min: {minVal_bst}, path: {minPath_bst}")
            print(f"Max: {maxVal_bst}, path: {maxPath_bst}")

            print("AVL: ")
            print(f"Min: {minVal_avl}, path: {minPath_avl}")
            print(f"Max: {maxVal_avl}, path: {maxPath_avl}")

            print("HMIN: ")
            print(f"Min: {minVal_hmin}, path: {minPath_hmin}")
            print(f"Max: {maxVal_hmin}, path: {maxPath_hmin}")

        case "2":

            values_bst = []
            values_avl = []
            
            key_value = int(input("Podaj wartość klucza: "))
            level_bst = f.find_level(bst_tree.node, key_value)
            level_avl = f.find_level(avl_tree.node, key_value)
            level_hmin, values_hmin = f.find_level_hmin(hmin, key_value)

            if level_bst is not None:
                print("BST: ")
                f.collect_level(bst_tree.node, level_bst, 0, values_bst)
                print(f"Klucz: {key_value}, poziom: {level_bst}, elementy na tym poziomie: {values_bst}")
            else:
                print("Brak wartości klucza w BST")

            if level_avl is not None:
                print("AVL: ")
                f.collect_level(avl_tree.node, level_avl, 0, values_avl)
                print(f"Klucz: {key_value}, poziom: {level_avl}, elementy na tym poziomie: {values_avl}")
            else:
                print("Brak wartości klucza w AVL")

            if level_hmin is not None:
                print("HMIN: ")
                print(f"Klucz: {key_value}, poziom: {level_hmin}, elementy na tym poziomie:{values_hmin}")

        case "3":

            print("BST: ")
            f.print_reverseTraverse(bst_tree.node)
            print(" ")
            print("AVL: ")
            f.print_reverseTraverse(avl_tree.node)
            print(" ")
            print(f"HMIN: {f.descending(hmin)}")

        case "4":

            key_value = int(input("Podaj wartość klucza: "))
            node_bst = f.find_node(bst_tree.node,key_value)
            node_avl = f.find_node(avl_tree.node, key_value)
            node_hmin, height_hmin, after_removal_hmin = f.get_heap_substructure(hmin, key_value)

            if node_bst is not None:
                print("BST: ")
                print("Poddrzewo: ", end="")
                f.print_inOrderTraverse(node_bst)
                print()
                print(f"Wysokość poddrzewa: {f.get_height(node_bst)}")
                bst_tree.node = f.remove_from_parent(bst_tree.node,key_value)
                print("Elementy pozostałe w drzewie: ", end="")
                f.print_inOrderTraverse(bst_tree.node)
                print()

            if node_avl is not None:
                print("AVL: ")
                print("Poddrzewo: ", end="")
                f.print_inOrderTraverse(node_avl)
                print()
                print(f"Wysokość poddrzewa: {f.get_height(node_avl)}")
                avl_tree.node = f.remove_from_parent(avl_tree.node,key_value)
                print("Elementy pozostałe w drzewie: ", end="")
                f.print_inOrderTraverse(avl_tree.node)
                print()

            if node_hmin is not None:
                print("HMIN: ")
                print(f"Poddrzewo: {node_hmin}")
                print(f"Wysokość poddrzewa: {height_hmin}")
                print(f"Elementy pozostałe w drzewie: {after_removal_hmin}")

        case "5":
            break

