import sys

In = sys.stdin.readline

N = int(In())
numberList = [0 for _ in range(10001)]

for _ in range(N):
    numberList[int(In()[:-1])] += 1

for i in range(10001):
    if numberList[i] != 0:
        for _ in range(numberList[i]):
            print(i)
