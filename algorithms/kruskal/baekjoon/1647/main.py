import sys

# class Edge:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __lt__(self, other):
#         return self.c < other.c


def get_parent(parents: list[int], node: int) -> int:
    if parents[node] != node:
        parents[node] = get_parent(parents, parents[node])
    return parents[node]


def union_parent(parents: list[int], node1: int, node2: int):
    node1_parent = get_parent(parents, node1)
    node2_parent = get_parent(parents, node2)

    if node1_parent > node2_parent:
        parents[parents[node1]] = node2_parent
        parents[node1] = node2_parent
    elif node1_parent < node2_parent:
        parents[parents[node2]] = node1_parent
        parents[node2] = node1_parent


def is_connected(parents: list[int], node1: int, node2: int) -> bool:
    return get_parent(parents, node1) == get_parent(parents, node2)


if __name__ == '__main__':
    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]
    graph = []
    total_cost = 0

    for i in range(N + 1):
        parents[i] = i

    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph.append([c, a, b])

    graph.sort()

    max_cost_edge = -1

    for c, a, b in graph:
        if not is_connected(parents, a, b):
            if c > max_cost_edge:
                max_cost_edge = c
            union_parent(parents, a, b)
            total_cost = total_cost + c

    total_cost -= max_cost_edge

    print(total_cost)
