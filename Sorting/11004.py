import sys

In = sys.stdin.readline
Out = sys.stdout.write

N, K = map(int, list(In()[:-1].split(' ')))

x = list(map(int, list(In()[:-1].split(' '))))

x.sort()

print(x[K-1])