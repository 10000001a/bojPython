import sys
from collections import deque

In = sys.stdin.readline

N, M = map(int, In().split())

comNet = {
    i: [] for i in range(1, N + 1)
}
DP = [0 for _ in range(N + 1)]
answer = ''


def BFS(start):
    count = 1
    # visited = {start}
    visited = [False] * (N + 1)
    will_visit = deque([start])
    visited[start] = True
    while will_visit:
        visiting = will_visit.popleft()
        for e in comNet[visiting]:
            if not visited[e]:
                visited[e] = True
                count += 1
                # visited.add(visiting)
                will_visit.append(e)
    return start, count


for _ in range(M):
    x, y = map(int, In().split())
    comNet[y].append(x)

maxHackable = -1
for i in range(1, N + 1):
    x = BFS(i)
    if x[1] > maxHackable:
        answer = (str(x[0]) + ' ')
        maxHackable = x[1]
    elif x[1] == maxHackable:
        answer += (str(x[0]) + ' ')

print(answer)
