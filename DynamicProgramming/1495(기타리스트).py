import sys

In = sys.stdin.readline

N, S, M = map(int, In()[:-1].split(' '))

volumeList = list(map(int, In()[:-1].split(' ')))

DP = [[False for _ in range(M + 1)] for _ in range(N + 1)]

DP[0][S] = True

for i, num in enumerate(volumeList):
    isExistTrue = False
    for j, data in enumerate(DP[i]):
        if data:
            if 0 <= j - num <= M:
                isExistTrue = True
                DP[i + 1][j - num] = True
            if 0 <= j + num <= M:
                isExistTrue = True
                DP[i + 1][j + num] = True
    if not isExistTrue:
        print(-1)
        exit()

for i in reversed(range(0, M + 1)):
    if DP[N][i]:
        print(i)
        exit()
