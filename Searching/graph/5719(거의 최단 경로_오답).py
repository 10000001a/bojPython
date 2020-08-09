import sys
import heapq

In = sys.stdin.readline

answer = ''


def dijkstra(graph, start, dest, prev=None):
    distances = {node: [float('inf'), start] for node in graph}

    distances[start][0] = 0

    queue = []

    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node][0] < current_distance:
            continue

        for adj, dis in graph[current_node].items():
            new_distance = dis + current_distance
            if new_distance < distances[adj][0]:
                distances[adj] = [new_distance, current_node]
                heapq.heappush(queue, [new_distance, adj])

    path = []
    if distances[dest][0] == float('inf'):
        return -1, path
    if prev is not None:
        if distances[dest][0] > prev:
            return distances[dest][0], path

    head = dest
    tail = distances[dest][1]
    while distances[head][0] > 0:
        path.append((tail, head))
        head = tail
        tail = distances[head][1]

    return distances[dest][0], path


while True:
    N, M = map(int, In().split())
    if N == 0 and M == 0:
        sys.stdout.write(answer[:-1])
        exit(0)
    S, D = map(int, In().split())

    graph = {i: {} for i in range(N)}

    for _ in range(M):
        U, V, P = map(int, In().split())
        graph[U][V] = P

    result, path = dijkstra(graph, S, D)
    while len(path) > 0:
        print(result, path)
        for tail, head in path:
            graph[tail].pop(head)
        result, path = dijkstra(graph, S, D, result)

    answer += (str(result) + '\n')
