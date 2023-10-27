
class Edge:
    def __init__(self, computer_a: int, computer_b: int, cost: int):
        self.computer_a = computer_a
        self.computer_b = computer_b
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def get_parent(computers_parents: list[int], computer_number: int):
    if computers_parents[computer_number] == computer_number:
        return computer_number
    else:
        computers_parents[computer_number] = \
            get_parent(computers_parents, computers_parents[computer_number])
        return computers_parents[computer_number]


def union(computers_parents: list[int], computer_number1: int, computer_number2: int):
    computer_number1_parent = get_parent(computers_parents, computer_number1)
    computer_number2_parent = get_parent(computers_parents, computer_number2)

    if computer_number1_parent > computer_number2_parent:
        computers_parents[computers_parents[computer_number1]] = computer_number2_parent
        computers_parents[computer_number1] = computer_number2_parent

    elif computer_number1_parent < computer_number2_parent:
        computers_parents[computers_parents[computer_number2]] = computer_number1_parent
        computers_parents[computer_number2] = computer_number1_parent


def is_connected(computer_parents: list[int], computer_number1: int, computer_number2: int):
    return get_parent(computer_parents, computer_number1) == \
        get_parent(computer_parents, computer_number2)


if __name__ == '__main__':
    total_cost = 0
    number_of_computers = int(input())
    number_of_edges = int(input())
    edges = []
    parents = [i for i in range(number_of_computers + 1)]

    for i in range(number_of_edges):
        a, b, c = map(int, input().split())
        edges.append(Edge(a, b, c))

    edges = sorted(edges)

    for edge in edges:
        a, b, cost = edge.computer_a, edge.computer_b, edge.cost
        if not is_connected(parents, a, b):
            total_cost = total_cost + cost
            union(parents, a, b)

    print(total_cost)
