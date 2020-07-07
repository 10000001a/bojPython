import sys

import heapq

In = sys.stdin.readline

N, M = map(int, In()[:-1].split(' '))

minHeap = list()

keyMap = [[] for _ in range(N + 1)]
seqList = list()
inDegree = [0 for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, In()[:-1].split(' '))

    keyMap[x].append(y)
    inDegree[y] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        heapq.heappush(minHeap, i)

while minHeap:
    x = heapq.heappop(minHeap)
    seqList.append(x)

    for i in keyMap[x]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(minHeap, i)

for i in seqList:
    print(i, end=' ')
