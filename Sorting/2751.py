import sys

In = sys.stdin.readline

N = int(In()[:-1])

list = []

for _ in range(N):
    list.append(int(In()[:-1]))

list.sort()

for data in list:
    sys.stdout.write(str(data) + '\n')