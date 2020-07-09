import sys

In = sys.stdin.readline

N, K = map(int, list(In()[:-1].split(' ')))
WeightIndex = 0
ValueIndex = 1

stuffList = [None]
DP = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, list(In()[:-1].split(' ')))

    stuffList.append((W, V))

for itemInd in range(1, N + 1):
    for weightInd in range(1, K + 1):
        x = weightInd - stuffList[itemInd][WeightIndex]
        if x < 0:
            DP[itemInd][weightInd] = DP[itemInd - 1][weightInd]
        else:
            DP[itemInd][weightInd] = \
                max(DP[itemInd - 1][x] + stuffList[itemInd][ValueIndex], DP[itemInd - 1][weightInd])

print(DP[N][K])
