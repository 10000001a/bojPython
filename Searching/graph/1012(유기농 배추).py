import sys
from collections import deque

In = sys.stdin.readline

T = int(In()[:-1])

answer = ''

for _ in range(T):
    M, N, K = map(int, In().split())

    cabbageMap = [[0 for _ in range(N)] for _ in range(M)]

    result = 0

    for _ in range(K):
        X, Y = map(int, In().split(' '))
        cabbageMap[X][Y] = 1
    for j in range(N):
        for i in range(M):
            if cabbageMap[i][j] == 1:
                result += 1
                will_visit = deque()
                cabbageMap[i][j] = 0

                if i < M - 1:
                    if cabbageMap[i + 1][j] == 1:
                        will_visit.append((i + 1, j))
                if j < N - 1:
                    if cabbageMap[i][j + 1] == 1:
                        will_visit.append((i, j + 1))

                while will_visit:
                    visiting = will_visit.popleft()

                    if visiting[0] > 0:
                        if cabbageMap[visiting[0] - 1][visiting[1]] == 1 and \
                                (visiting[0] - 1, visiting[1]) not in will_visit:
                            will_visit.append((visiting[0] - 1, visiting[1]))
                    if visiting[1] > 0:
                        if cabbageMap[visiting[0]][visiting[1] - 1] == 1 and \
                                (visiting[0], visiting[1] - 1) not in will_visit:
                            will_visit.append((visiting[0], visiting[1] - 1))
                    if visiting[0] < M - 1:
                        if cabbageMap[visiting[0] + 1][visiting[1]] == 1 and \
                                (visiting[0] + 1, visiting[1]) not in will_visit:
                            will_visit.append((visiting[0] + 1, visiting[1]))
                    if visiting[1] < N - 1:
                        if cabbageMap[visiting[0]][visiting[1] + 1] == 1 and \
                                (visiting[0], visiting[1] + 1) not in will_visit:
                            will_visit.append((visiting[0], visiting[1] + 1))

                    cabbageMap[visiting[0]][visiting[1]] = 0

    answer += (str(result) + '\n')

sys.stdout.write(answer[:-1])
