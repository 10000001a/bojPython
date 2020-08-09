import sys
import heapq
from collections import deque

In = sys.stdin.readline
answer = ''


def dijkstra():
    queue = [(0, S)]
    distance[S] = 0

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distance[current_vertex]:
            continue

        for next_vertex, weight in adj[current_vertex]:

            cost = current_distance + weight
            if distance[next_vertex] > cost and not dropped[current_vertex][next_vertex]:
                distance[next_vertex] = cost
                heapq.heappush(queue, (cost, next_vertex))


def bfs():
    queue = deque([(D, distance[D])])

    while queue:
        visiting_node, distance_from_next = queue.popleft()
        if visiting_node == S:
            continue
        for start, weight in reverse_adj[visiting_node]:
            if distance[visiting_node] - weight == distance[start]:
                queue.append((start, weight))
                dropped[start][visiting_node] = True


while True:
    N, M = map(int, In().split())
    if N == 0 and M == 0:
        sys.stdout.write(answer[:-1])
        exit(0)
    S, D = map(int, In().split())

    adj = [[] for _ in range(N)]
    reverse_adj = [[] for _ in range(N)]

    for _ in range(M):
        X, Y, weight = map(int, In().split())
        adj[X].append((Y, weight))
        reverse_adj[Y].append((X, weight))

    dropped = [[False] * N for _ in range(N)]
    distance = [float('inf')] * N
    dijkstra()
    if distance[D] == float('inf'):
        answer += '-1\n'
        continue
    bfs()

    distance = [float('inf')] * N
    dijkstra()
    if distance[D] == float('inf'):
        answer += '-1\n'
    else:
        answer += str(distance[D]) + '\n'
