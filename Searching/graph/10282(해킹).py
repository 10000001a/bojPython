import sys
import heapq

In = sys.stdin.readline

testNum = int(In()[:-1])


def dijkstra(graph, start):
    distance = [float('inf') for _ in range(len(graph) + 1)]
    distance[0] = float('inf')
    distance[start] = 0
    queue = [[0, start]]
    while queue:
        data = heapq.heappop(queue)
        for x, y in graph[data[1]].items():
            if distance[x] > distance[data[1]] + y:
                distance[x] = distance[data[1]] + y
                heapq.heappush(queue, [y, x])

    time = -1
    hackedComCount = 0
    for vertex, weight in enumerate(distance):
        if vertex == 0:
            pass
        if weight >= 0 and type(weight) == int:
            hackedComCount += 1
            if weight > time:
                time = weight

    return hackedComCount, time


answer = ''
for _ in range(testNum):
    n, d, c = map(int, In().split())

    graph = {
        i: dict() for i in range(1, n + 1)
    }
    for i in range(d):
        a, b, s = map(int, In().split())
        graph[b][a] = s

    result = dijkstra(graph, c)
    answer += str(result[0]) + ' '
    answer += str(result[1]) + '\n'

sys.stdout.write(answer)