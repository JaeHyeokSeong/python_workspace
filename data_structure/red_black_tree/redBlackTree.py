from node import Node


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.inserted_node = None

    def __inorder_traversal_data(self, node: Node | None, result: list[int]):
        if node is not None:
            self.__inorder_traversal_data(node.left, result)
            result.append(node.data)
            self.__inorder_traversal_data(node.right, result)

    def inorder_traversal_data(self) -> list[int]:
        result = []
        self.__inorder_traversal_data(self.root, result)
        return result

    def __inorder_traversal_color(self, node: Node | None, result: list[str]):
        if node is not None:
            self.__inorder_traversal_color(node.left, result)
            result.append(node.color)
            self.__inorder_traversal_color(node.right, result)

    def inorder_traversal_color(self) -> list[str]:
        result = []
        self.__inorder_traversal_color(self.root, result)
        return result

    def __find_data(self, root: Node, data: int) -> Node | None:
        tmp_node = root
        while tmp_node is not None:
            if tmp_node.data == data:
                return tmp_node
            elif tmp_node.data > data:
                tmp_node = tmp_node.left
            else:
                tmp_node = tmp_node.right
        return None

    def find(self, data) -> Node | None:
        return self.__find_data(self.root, data)

    def __left_rotate(self, node: Node):
        right_node = node.right
        parent_node = node.parent

        if right_node.left is not None:
            right_node.left.parent = node

        node.right = right_node.left
        node.parent = right_node
        right_node.left = node
        right_node.parent = parent_node

        if parent_node is None:
            self.root = right_node
        else:
            if parent_node.left is node:
                parent_node.left = right_node
            elif parent_node.right is node:
                parent_node.right = right_node

    def __right_rotate(self, node: Node):
        left_node = node.left
        parent_node = node.parent

        if left_node.right is not None:
            left_node.right.parent = node

        node.left = left_node.right
        node.parent = left_node
        left_node.right = node
        left_node.parent = parent_node

        if parent_node is None:
            self.root = left_node
        else:
            if parent_node.left is node:
                parent_node.left = left_node
            elif parent_node.right is node:
                parent_node.right = left_node

    def insert(self, data: int):
        self.root = self.__insert_node(self.root, data, None)
        self.__balancing(self.inserted_node)

    def __insert_node(self, current_node: Node, data: int, parent_node: Node | None) -> Node:
        if current_node is None:
            current_node = Node(data=data)
            current_node.parent = parent_node
            self.inserted_node = current_node
        else:
            if data < current_node.data:
                current_node.left = self.__insert_node(current_node.left, data, current_node)
            else:
                current_node.right = self.__insert_node(current_node.right, data, current_node)
        return current_node

    def __balancing(self, node: Node):
        parent_node = node.parent

        # node is located at root node == parent_node is None
        if parent_node is None:
            node.color = 'Black'
        # node is not located at root node
        else:
            # double red happened
            if parent_node.color == 'Red':
                grandparent_node = parent_node.parent
                uncle_node = None
                if grandparent_node.left == parent_node:
                    uncle_node = grandparent_node.right
                else:
                    uncle_node = grandparent_node.left

                # perform recoloring
                if uncle_node is not None and uncle_node.color == 'Red':
                    parent_node.color = uncle_node.color = 'Black'
                    grandparent_node.color = 'Red'
                    self.__balancing(grandparent_node)
                # perform restructuring == uncle_node is None or uncle_node.color == 'Black'
                else:
                    # LL case
                    if parent_node is grandparent_node.left and parent_node.left is node:
                        parent_node.color, grandparent_node.color = grandparent_node.color, \
                            parent_node.color
                        self.__right_rotate(grandparent_node)
                    # LR case
                    elif parent_node is grandparent_node.left and parent_node.right is node:
                        self.__left_rotate(parent_node)
                        node.color, grandparent_node.color = grandparent_node.color, node.color
                        self.__right_rotate(grandparent_node)
                    # RR case
                    elif parent_node is grandparent_node.right and parent_node.right is node:
                        grandparent_node.color, parent_node.color = parent_node.color, grandparent_node.color
                        self.__left_rotate(grandparent_node)
                    # RL case
                    elif parent_node is grandparent_node.right and parent_node.left is node:
                        self.__right_rotate(parent_node)
                        node.color, grandparent_node.color = grandparent_node.color, node.color
                        self.__left_rotate(grandparent_node)

    def remove(self, data):
        remove_node = self.__get_remove_node(self.root, data)
        # data has found
        if remove_node is not None:
            self.__remove_node(remove_node, True)

    def __get_remove_node(self, node: Node | None, data: int):
        if node is None:
            return None
        elif node.data > data:
            return self.__get_remove_node(node.left, data)
        elif node.data < data:
            return self.__get_remove_node(node.right, data)
        else:
            left_node, right_node = node.left, node.right
            if left_node is not None and right_node is not None:
                min_node = self.find_min_node(node.right)
                node.data, min_node.data = min_node.data, node.data
                return min_node
            else:
                return node

    def __remove_node(self, remove_node: Node | None, status: bool, tmp_parent=None):
        if remove_node is None:
            remove_node_color = 'Black'
        else:
            remove_node_color = remove_node.color

        # if remove node color is red there is nothing to do to maintain
        # red black tree properties
        # however, if color is black, then we need some works to
        # maintain red black tree properties
        if remove_node_color == 'Red':
            # if color is red, then it means that it has parent node (not None)
            r_parent_node = remove_node.parent
            if r_parent_node.left is remove_node:
                r_parent_node.left = None
            elif r_parent_node.right is remove_node:
                r_parent_node.right = None
        elif remove_node_color == 'Black':
            r_parent_node = None
            r_sibling_node = None

            if remove_node is not None:
                r_parent_node = remove_node.parent
            else:
                r_parent_node = tmp_parent

            # remove_node is located at root node
            if r_parent_node is None:
                # only one node is existed in red black tree
                if remove_node.left is None and remove_node.right is None:
                    self.root = None
                # change child node to root node
                # find where is the child node is it in left or right
                else:
                    r_child_node = remove_node.left
                    if r_child_node is None:
                        r_child_node = remove_node.right
                    # property two: root not is always black
                    if r_child_node.color == 'Red':
                        r_child_node.color = 'Black'
                    r_child_node.parent = None
                    self.root = r_child_node
            else:
                # implement case 4
                r_child_node = None

                if remove_node is not None:
                    if remove_node.left is not None:
                        r_child_node = remove_node.left
                    elif remove_node.right is not None:
                        r_child_node = remove_node.right
                else:
                    r_child_node = remove_node

                # doubly black case
                if r_child_node is None or r_child_node.color == 'Black' or status is False:
                    # case 4
                    # find where is the sibling node
                    if r_parent_node.left is remove_node:
                        r_sibling_node = r_parent_node.right
                        r_sibling_right_child = r_sibling_node.right
                        r_sibling_left_child = r_sibling_node.left

                        if status is True:
                            # remove remove_node (remove node)
                            r_parent_node.left = r_child_node
                            if r_child_node is not None:
                                r_child_node.parent = r_parent_node

                        # case 4
                        if r_sibling_right_child is not None:
                            if r_sibling_node.color == 'Black' and r_sibling_right_child.color == 'Red':
                                r_sibling_node.color = r_parent_node.color
                                r_sibling_right_child.color = 'Black'
                                r_parent_node.color = 'Black'
                                self.__left_rotate(r_parent_node)
                                return
                        # case 3
                        if r_sibling_left_child is not None:
                            if r_sibling_node.color == 'Black' and r_sibling_left_child.color == 'Red' \
                                 and (r_sibling_right_child is None or r_sibling_right_child.color == 'Black'):
                                # change color left_sibling node and sibling node
                                r_sibling_left_child.color, r_sibling_node.color = r_sibling_node.color, \
                                    r_sibling_left_child.color
                                # right rotate for sibling node
                                self.__right_rotate(r_sibling_node)
                                # perform case 4
                                r_sibling_left_child.color = r_parent_node.color
                                r_parent_node.color = 'Black'
                                r_sibling_node.color = 'Black'
                                self.__left_rotate(r_parent_node)
                                return
                        # case 2
                        if r_sibling_node.color == 'Black' and (r_sibling_left_child is None or r_sibling_left_child.color == 'Black') \
                                and (r_sibling_right_child is None or r_sibling_right_child.color == 'Black'):
                            r_sibling_node.color = 'Red'
                            # parent color is red that means red and black case
                            if r_parent_node.color == 'Red':
                                r_parent_node.color = 'Black'
                            # parent color is black that means doubly black case
                            else:
                                # parent node is located at root node
                                if r_parent_node.parent is None:
                                    r_parent_node.color = 'Black'
                                # doubly black
                                else:
                                    self.__remove_node(r_parent_node, False)
                            return
                        # case 1
                        if r_sibling_node.color == 'Red':
                            # change parent color and sibling color
                            r_sibling_node.color, r_parent_node.color = r_parent_node.color, r_sibling_node.color
                            self.__left_rotate(r_parent_node)
                            self.__remove_node(r_child_node, False, tmp_parent=r_parent_node)

                    # sibling node is located in left side
                    elif r_parent_node.right is remove_node:
                        r_sibling_node = r_parent_node.left
                        r_sibling_left_child = r_sibling_node.left
                        r_sibling_right_child = r_sibling_node.right

                        if status is True:
                            # remove remove_node (remove node)
                            r_parent_node.right = r_child_node
                            if r_child_node is not None:
                                r_child_node.parent = r_parent_node

                        # case 4
                        if r_sibling_left_child is not None:
                            if r_sibling_node.color == 'Black' and r_sibling_left_child.color == 'Red':
                                r_sibling_node.color = r_parent_node.color
                                r_sibling_left_child.color = 'Black'
                                r_parent_node.color = 'Black'
                                self.__right_rotate(r_parent_node)
                                return
                        # case 3
                        if r_sibling_right_child is not None:
                            if r_sibling_node.color == 'Black' and r_sibling_right_child.color == 'Red' \
                                 and (r_sibling_left_child is None or r_sibling_left_child.color == 'Black'):
                                r_sibling_right_child.color, r_sibling_node.color = r_sibling_node.color, \
                                    r_sibling_right_child.color
                                self.__left_rotate(r_sibling_node)
                                r_sibling_right_child.color = r_parent_node.color
                                r_parent_node.color = 'Black'
                                r_sibling_node.color = 'Black'
                                self.__right_rotate(r_parent_node)
                                return
                        # case 2
                        if r_sibling_node.color == 'Black' and (r_sibling_left_child is None or r_sibling_left_child.color == 'Black') \
                                and (r_sibling_right_child is None or r_sibling_right_child.color == 'Black'):
                            r_sibling_node.color = 'Red'
                            # parent color is red that means red and black case
                            if r_parent_node.color == 'Red':
                                r_parent_node.color = 'Black'
                            # parent color is black that means doubly black case
                            else:
                                # parent node is located at root node
                                if r_parent_node.parent is None:
                                    r_parent_node.color = 'Black'
                                # doubly black
                                else:
                                    self.__remove_node(r_parent_node, False)
                            return
                        # case 1
                        if r_sibling_node.color == 'Red':
                            # change parent color and sibling color
                            r_sibling_node.color, r_parent_node.color = r_parent_node.color, r_sibling_node.color
                            self.__right_rotate(r_parent_node)
                            self.__remove_node(r_child_node, False, tmp_parent=r_parent_node)

    def find_min_node(self, node: Node) -> Node | None:
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node
