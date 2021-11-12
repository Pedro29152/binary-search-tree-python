from BinaryTree.Node import Node

class BinarySearchTree():
    def __init__(self, root: Node = None):
        self.root = root

    def add_node(self, id: int, value = None):
        new_node = Node(id, value=value)
        if not self.root:
            self.root = new_node
        else:
            self.root.add(new_node)
        return new_node

    def remove_node(self, id: int):
        if not self.root:
            return None

        node = self.root.get_node(id)
        if not node:
            return None
        
        if not node.parent:
            if not node.right and not node.left:
                self.root = None
            elif node.right and not node.left:
                self.root = node.right
            elif node.left and not node.right:
                self.root = node.left
            else:
                min_node = node.right.get_min_node()
                self.remove_node(min_node.id)
                self.root.id = min_node.id
                self.root.value = min_node.value
        else:
            parent_side = ''
            if node.parent.right:
                parent_side = 'right' if node.parent.right.id == node.id else 'left'
            else:
                parent_side = 'left'
            
            if not node.right and not node.left:
                node.parent[parent_side] = None
            elif node.right and not node.left:
                node.parent[parent_side] = node.right
            elif node.left and not node.right:
                node.parent[parent_side] = node.left
            else:
                min_node = node.right.get_min_node()
                self.remove_node(min_node.id)
                node.parent[parent_side].id = min_node.id
                node.parent[parent_side].value = min_node.value

        return node
                
    def get_node(self, id: int):
        return self.root.get_node(id)

    def get_min(self):
        return self.root.get_min_node()

    def get_max(self):
        return self.root.get_max_node()

    def get_list(self, max_size: int=None, ascending: bool=True):
        return self.root.get_sorted_list(max_size=max_size, ascending=ascending)
    
    def load_from_list(self, load_list: 'list'):
        for item in load_list:
            try:
                self.add_node(item)
            except ValueError:
                pass
        return self

    def get_size(self):
        if not self.root:
            return 0
        return self.root.get_size()

    def get_height(self):
        return self.root.get_height()

    def print_tree(self):
        if not self.root:
            return
        
        altura = self.root.get_height()
        str_size = 3
        nivel = [[str_size * ' ' for j in range(pow(2,i))] for i in range(altura)]
        self.__fill_matrix(nivel, self.root)
        for idx, nv in enumerate(nivel):
            prefix = pow(2,altura-(idx)) * ' '
            separator = self.__get_separator(altura, idx+1, str_size) * ' '
            content = separator.join([self.__get_fill(str(i), str_size) + str(i) for i in nv])
            print(prefix + content)
    
    def __get_fill(self, str: str, size: int, fill: str = ' '):
        if len(str) > size:
            return ''
        return (size - len(str))  * fill

    def __get_separator(self, h: int, cur_h: int, num_size: int = 3):
        if h <= cur_h:
            return 1
        if cur_h == h -1:
            return 2 + num_size
        
        return (self.__get_separator(h, cur_h+1, num_size) * 2) + num_size

    def __fill_matrix(self, arr: 'list', node: Node, cur_pos: int = 0, cur_h: int = 0):
        arr[cur_h][cur_pos] = node.id

        if node.right:
            self.__fill_matrix(arr, node.right, cur_pos=(2 * cur_pos) + 1, cur_h=cur_h+1)
        if node.left:
            self.__fill_matrix(arr, node.left, cur_pos=(2 * cur_pos), cur_h=cur_h+1)

    def __get_next_rl(self, tree_arr: 'list', h: int, pos: int):
        try:
            start_pos_ntx_lvl = 2*(pos)
            return tree_arr[h+1][start_pos_ntx_lvl:start_pos_ntx_lvl+2]
        except IndexError:
            return None
