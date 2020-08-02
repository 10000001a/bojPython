import sys
from collections import deque

sys.setrecursionlimit(10000)

MAX = 100001
N, K = map(int, sys.stdin.readline()[:-1].split())
array = [0] * MAX


def BFS(start):
    will_visit = deque([start])
    while will_visit:
        visiting = will_visit.popleft()
        if visiting == K:
            return array[visiting]
        for next in (visiting - 1, visiting + 1, visiting * 2):
            if 0 <= next < MAX and not array[next]:
                array[next] = array[visiting] + 1
                will_visit.append(next)


print(BFS(N))
