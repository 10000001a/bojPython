import sys

sys.setrecursionlimit(100000)

In = sys.stdin.readline
Out = sys.stdout.write

N = int(In()[:-1])

brickList = [(0, 0, 0, 0)]
answer = [[i] for i in range(0, N + 1)]


def indexToHeight(index):
    return brickList[index][2]


def getTotalHeight(indexList):
    return sum(list(map(indexToHeight, indexList)))


for i in range(N):
    area, height, weight = map(int, In().split())
    brickList.append((i + 1, area, height, weight))

brickList.sort(key=lambda brick: brick[3])

for i in range(2, N + 1):
    maxTower = answer[i]
    for j in range(1, i):
        if brickList[i][1] > brickList[j][1] and getTotalHeight(maxTower) < getTotalHeight(answer[i] + answer[j]):
            maxTower = answer[i] + answer[j]
    answer[i] = maxTower

result = []
for data in answer:
    if getTotalHeight(result) < getTotalHeight(data):
        result = data
print(len(result))
for data in reversed(result):
    print(brickList[data][0])
