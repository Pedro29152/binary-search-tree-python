import random, timeit, sys
from BinaryTree.BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    size = 100
    try:
        size = int(sys.argv[1])
    except:
        pass

    max_val = size*10
    tree = BinarySearchTree()

    arr = []
    for i in range(size):
        try:
            val = random.randint(0, max_val)
            tree.add_node(val)
            arr.append(val)
        except ValueError:
            pass

    print("Tree height/depth: ", tree.get_height())
    print("Number of elements inserted: ", tree.get_size())
    print("Tree max value: ", tree.get_max().id)
    print("Tree min value: ", tree.get_min().id)
    print("Tree as a sorted list: ", tree.get_list())
    print("Tree as an inverted sorted list: ", tree.get_list(ascending=False))
    try:
        show = int(input('Show tree? (1 - Yes): '))
        if show == 1:
            print('TREE---------------------------------')
            tree.print_tree()
            print('-------------------------------------')
    except:
        pass