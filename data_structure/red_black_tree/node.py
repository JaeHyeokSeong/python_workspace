class Node:
    def __init__(self, data: int | None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'Red'
