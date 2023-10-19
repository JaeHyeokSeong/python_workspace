from node import Node

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.inserted_node = None

    def __find_data(self, root, data) -> Node | None:
        if root is None or root.data == data:
            return root
            # return None or 데이터가 포함되어져있는 노드
        elif root.data > data:
            self.__find_data(root.left, data)
        else:
            self.__find_data(root.right, data)

    def find(self, data):
        node = self.__find_data(self.root, data)
        if node is not None:
            print(f'data: {data} has found')
        else:
            print(f'data: {data} has not found')
        return node

