import sys

In = sys.stdin.readline

inputString = [None] + list(In()[:-1])
lenInput = len(inputString)
targetString = [None] + list(In()[:-1])
lenTarget = len(targetString)
DP = [[0 for _ in range(lenTarget)] for _ in range(lenInput)]

for i in range(1, lenInput):
    for j in range(1, lenTarget):
        if inputString[i] == targetString[j]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[lenInput - 1][lenTarget - 1])
