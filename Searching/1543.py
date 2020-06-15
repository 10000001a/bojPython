import sys

In = sys.stdin.readline

doc = In()[:-1]

keyword = In()[:-1]

checkpoint = 0
answer = 0
i = 0

while i <= len(doc) - len(keyword):
    checkpoint = 0
    while True:
        if doc[i + checkpoint] == keyword[checkpoint]:
            if checkpoint == len(keyword) - 1:
                answer += 1
                i += (len(keyword)-1)
                break
            else:
                checkpoint += 1
        else:
            break
    i += 1

print(answer)