import sys

In = sys.stdin.readline
answer = ''
N = list(map(str, In()[:-1]))
N.sort(reverse=True)

for char in N:
    answer += char

print(answer)