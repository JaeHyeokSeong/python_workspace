total_element = 3
graph = [[] for i in range(total_element + 1)]
result = [0 for j in range(total_element + 1)]
visited = None


def dfs(node) -> bool:
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        if result[next_node] == 0 or dfs(result[next_node]):
            result[next_node] = node
            return True

    return False


if __name__ == '__main__':
    graph[1].append(1)
    graph[1].append(2)
    graph[1].append(3)
    graph[2].append(1)
    graph[3].append(2)

    for i in range(1, total_element + 1):
        visited = [False for j in range(total_element + 1)]
        dfs(i)

    for i in range(1, total_element + 1):
        if result[i] != 0:
            print(f'{result[i]} -> {i}')
