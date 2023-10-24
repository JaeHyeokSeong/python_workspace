# references:
# [1]: https://blog.naver.com/ndb796/221230994142

from edge import Edge


def get_parent_node(parents: list[int], node: int) -> int:
    if parents[node] == node:
        return node
    else:
        parents[node] = get_parent_node(parents, parents[node])
        return parents[node]


def union(parents: list[int], node1: int, node2: int):
    node1_parent = get_parent_node(parents, node1)
    node2_parent = get_parent_node(parents, node2)

    if node1_parent > node2_parent:
        parents[node1] = node2_parent
    else:
        parents[node2] = node1_parent


def is_connected(parents: list[int], node1: int, node2: int) -> bool:
    node1_parent = get_parent_node(parents, node1)
    node2_parent = get_parent_node(parents, node2)
    return node1_parent == node2_parent


if __name__ == '__main__':
    total_nodes = 7
    nodes_parents = [0 for i in range(total_nodes + 1)]
    for i in range(1, total_nodes + 1):
        nodes_parents[i] = i
    edges = [
        Edge(1, 2, 67),
        Edge(1, 4, 28),
        Edge(1, 5, 17),
        Edge(1, 7, 12),
        Edge(2, 4, 24),
        Edge(2, 5, 62),
        Edge(3, 5, 20),
        Edge(3, 6, 37),
        Edge(4, 7, 13),
        Edge(5, 6, 45),
        Edge(5, 7, 73)
    ]
    edges = sorted(edges)

    total_cost = 0

    for edge in edges:
        n1 = edge.node1
        n2 = edge.node2
        if not is_connected(nodes_parents, n1, n2):
            union(nodes_parents, n1, n2)
            total_cost = total_cost + edge.cost

    print(f'total cost: {total_cost}')