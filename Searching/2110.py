import sys
import collections

In = sys.stdin.readline

N, C = map(int, list(In()[:-1].split(' ')))

location = collections.deque('')

for _ in range(N):
    location.append(int(In()[:-1]))

location = sorted(location)

maxGap = location[-1] - location[0]
minGap = 1
answer = 0


while minGap <= maxGap:
    mid = (minGap + maxGap) // 2
    wifiCount = 0
    pivot = 0
    for i in enumerate(location):
        if i[0] == 0:
            wifiCount += 1
            pivot = i[1]
        elif i[1] >= pivot + mid:
            wifiCount += 1
            pivot = i[1]

    if wifiCount < C:
        maxGap = mid - 1
    elif wifiCount >= C:
        minGap = mid + 1
        answer = mid

print(answer)