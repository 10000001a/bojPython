import sys

N = int(sys.stdin.readline()[:-1])
if N == 0:
    print(0)
    exit()
if N == 1:
    print(1)
    exit()
if N == 2:
    print(2)
    exit()
DP = [0 for _ in range(N + 1)]

DP[1] = 1
DP[2] = 2

for i in range(3, N+1):
    DP[i] = (DP[i - 1] + DP[i - 2]) % 15746

print(DP[N])