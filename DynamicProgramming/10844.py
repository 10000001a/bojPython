import sys

In = sys.stdin.readline

N = int(In()[:-1])

countList = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(N - 1):
    countList = [
        countList[1],
        countList[0] + countList[2],
        countList[1] + countList[3],
        countList[2] + countList[4],
        countList[3] + countList[5],
        countList[4] + countList[6],
        countList[5] + countList[7],
        countList[6] + countList[8],
        countList[7] + countList[9],
        countList[8]
    ]

print(sum(countList) % 1000000000)