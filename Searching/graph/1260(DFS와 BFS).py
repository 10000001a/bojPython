import sys
from collections import deque

In = sys.stdin.readline

N, M, V = map(int, In()[:-1].split(' '))

graph = {
    i: [] for i in range(1, N + 1)
}

for i in range(M):
    start, end = map(int, In()[:-1].split(' '))
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()


# print(graph)

def DFS(graph, start):
    visited = []
    will_visit = deque([start])

    while will_visit:
        visiting = will_visit.popleft()
        if visiting not in visited:
            tmp = len(graph[visiting]) - 1
            while tmp >= 0:
                will_visit.appendleft(graph[visiting][tmp])
                tmp -= 1
            visited.append(visiting)

    answer = ''
    for data in visited:
        answer += str(data) + ' '
    sys.stdout.write(answer[:-1] + '\n')


def BFS(graph, start):
    visited = []
    will_visit = deque([start])

    while will_visit:
        visiting = will_visit.popleft()
        if visiting not in visited:
            tmp = 0
            while tmp <= (len(graph[visiting]) - 1):
                will_visit.append(graph[visiting][tmp])
                tmp += 1
            visited.append(visiting)

    answer = ''
    for data in visited:
        answer += str(data) + ' '
    sys.stdout.write(answer[:-1] + '\n')


DFS(graph, V)
BFS(graph, V)
