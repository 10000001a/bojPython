import sys
from collections import deque

In = sys.stdin.readline

N = int(In()[:-1])
E = int(In()[:-1])

computerNet = {
    i: [] for i in range(1, N + 1)
}

answer = 0

for i in range(E):
    x, y = map(int, In()[:-1].split())
    computerNet[x].append(y)
    computerNet[y].append(x)


def BFS():
    visited = [1]
    will_visit = deque(computerNet[1])
    while will_visit:
        visiting = will_visit.popleft()
        if visiting not in visited:
            will_visit.extend(computerNet[visiting])
            visited.append(visiting)

    return len(visited) - 1


print(BFS())
