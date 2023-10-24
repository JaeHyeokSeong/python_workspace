
class Edge:
    def __init__(self, node1: int, node2: int, cost: int):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
