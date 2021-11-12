class Node():
    def __init__(self, id: int, value = None, right: 'Node' = None, left: 'Node' = None):
        self.id = id
        self.value = value
        self.right = right
        self.left = left
        self.parent: 'Node' = None
  
    def add(self, node: 'Node'):
        if not node:
            raise ValueError('node value invalid')

        if node.id == self.id:
            raise ValueError('The id sent is alredy on the tree')

        if node.id > self.id:
            if not self.right:
                node.parent = self
                self.right = node
            else:
                self.right.add(node)
        if node.id < self.id:
            if not self.left:
                node.parent = self
                self.left = node
            else:
                self.left.add(node)

    def get_size(self):
        size_l = self.left.get_size() if self.left else 0
        size_r = self.right.get_size() if self.right else 0

        return 1 + size_l + size_r

    def get_height(self):
        h_l = self.left.get_height() if self.left else 0
        h_r = self.right.get_height() if self.right else 0

        if h_r > h_l:
            return 1 + h_r
        return 1 + h_l

    def get_node(self, id: int):
        if self.id == id:
            return self

        if id > self.id:
            if self.right:
                return self.right.get_node(id)

        if id < self.id:
            if self.left:
                return self.left.get_node(id)
        
        return None

    def get_min_node(self):
        if not self.left:
            return self
        return self.left.get_min_node()

    def get_max_node(self):
        if not self.right:
            return self
        return self.right.get_max_node()

    def get_sorted_list(self, max_size: int=None, ascending: bool=True):
        if max_size == None:
            return self.__get_list(ascending)
        return self.__get_list_by_size(max_size, ascending)

    def __get_list(self, ascending: bool):
        list_e = self.left.__get_list(ascending) if self.left else []
        list_d = self.right.__get_list(ascending) if self.right else []
        
        if ascending:
            return list_e + [self.id] + list_d
        return list_d + [self.id] + list_e

    def __get_list_by_size(self, max_size: int, ascending: bool):
        if ascending:
            st = 'left'
            fi = 'right'
        else:
            st = 'right'
            fi = 'left'
        
        list_st = self[st].__get_list_by_size(max_size=max_size, ascending=ascending) if self[st] else []
        if max_size <= len(list_st):
            return list_st
        elif max_size <= len(list_st) + 1:
            return list_st + [self.id]
        else:
            curr_size = len(list_st) + 1
            list_fi = self[fi].__get_list_by_size(max_size=max_size-curr_size, ascending=ascending) if self[fi] else []
            return list_st + [self.id] + list_fi

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __str__(self):
        str_e = self.left.__str__() if self.left else None
        str_d = self.right.__str__() if self.right else None
        if not (str_e or str_d):
            return f'[({self.id})]'
        return f'[({self.id}) {str_e}, {str_d}]'        
