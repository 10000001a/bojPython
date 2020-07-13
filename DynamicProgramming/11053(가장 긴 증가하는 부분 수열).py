import sys

In = sys.stdin.readline

N = int(In()[:-1])

A = list(map(int, In()[:-1].split(' ')))

answer = [1] * len(A)

for i in range(1, len(A)):
    for j in range(0, i):
        if A[i] > A[j]:
            answer[i] = max(answer[i], answer[j] + 1)

print(max(answer))