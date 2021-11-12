import random, timeit
from BinaryTree.BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    arvore = BinarySearchTree()

    tam = 6
    max_val = 50
    arr = []
    for i in range(tam):
        val = random.randint(0, max_val)
        try:
            arvore.add_node(val)
            arr.append(val)
        except ValueError:
            pass
    
    arvore2 = BinarySearchTree(arvore.raiz)
    e = arr[random.randint(0, len(arr) - 1)]
    arvore.print_tree()
    arvore2.print_tree()

