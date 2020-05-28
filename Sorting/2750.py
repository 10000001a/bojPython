import sys

In = sys.stdin.readline
Out = sys.stdout.write

N = int(In())
answer = []
for _ in range(N):
    answer.append(int(In()))

answer.sort()

for data in answer:
    Out(str(data) + '\n')
