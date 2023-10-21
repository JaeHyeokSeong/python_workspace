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
        pass

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

    def __remove_node(self, remove_node: Node):
        child_node = sibling_node = None
        parent_node = remove_node.parent

        # 자식이 어디에 위치해 있는지 확인하기
        if remove_node.left is not None:
            child_node = remove_node.left
        elif remove_node.right is not None:
            child_node = remove_node.right

        # 만약에 parent_node 가 None 이라는 의미는 총 노드의 수가 하나만 있다는
        # 의미이다.
        if parent_node is None:
            self.root = None
            return
        elif remove_node is parent_node.left:
            sibling_node = parent_node.right
        elif remove_node is parent_node.right:
            sibling_node = parent_node.left

        if child_node is None:
            # 임시 객체 만들기
            child_node = Node(None)
            child_node.parent = remove_node
            child_node.color = 'Black'

        if remove_node.color == 'Red' or child_node.color == 'Red':
            if child_node.data is not None:
                child_node.parent = parent_node
                child_node.color = 'Black'
                if parent_node.left is remove_node:
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node
            else:
                if parent_node.left is remove_node:
                    parent_node.left = None
                else:
                    parent_node.right = None
        elif remove_node.color == 'Black' and child_node.color == 'Black':
            child_node.parent = parent_node
            if remove_node is parent_node.left:
                if child_node.data is None:
                    parent_node.left = None
                else:
                    parent_node.left = child_node
            elif remove_node is parent_node.right:
                if child_node.data is None:
                    parent_node.right = None
                else:
                    parent_node.left = child_node

    def find_min_node(self, node: Node) -> Node | None:
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node
