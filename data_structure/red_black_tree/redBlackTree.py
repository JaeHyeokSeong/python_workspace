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

    def __find_data(self, root, data) -> Node | None:
        if root is None or root.data == data:
            # return None or 데이터가 포함되어져있는 노드
            return root
        elif root.data > data:
            self.__find_data(root.left, data)
        else:
            self.__find_data(root.right, data)

    def find(self, data) -> Node | None:
        node = self.__find_data(self.root, data)
        if node is not None:
            print(f'data: {data} has found')
        else:
            print(f'data: {data} has not found')
        return node

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
