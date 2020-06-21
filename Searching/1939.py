import sys
from collections import deque

In = sys.stdin.readline

N, M = map(int, list(In()[:-1].split(' ')))

weightArray = [[] for _ in range(N + 1)]
minWeight = 1000000000
maxWeight = 1


def bfs(c):
    queue = deque([facA])
    visited = [False] * (N + 1)
    visited[facA] = True
    while queue:
        x = queue.popleft()
        for y, weight in weightArray[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[facB]


for _ in range(M):
    a, b, c = map(int, list(In()[:-1].split(' ')))
    weightArray[a].append((b, c))
    weightArray[b].append((a, c))
    maxWeight = max(c, maxWeight)
    minWeight = min(c, minWeight)

facA, facB = map(int, list(In()[:-1].split(' ')))

# if facA > N or facB > N:
#     print(0)
#     exit()
#
# if not weightArray[facA] or not weightArray[facB]:
#     print(0)
#     exit()

answer = minWeight

while minWeight <= maxWeight:  # 이진 탐색
    mid = (minWeight + maxWeight) // 2

    if bfs(mid):
        result = mid
        minWeight = mid + 1
    else:
        maxWeight = mid - 1

print(answer)
