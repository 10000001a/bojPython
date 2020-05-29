import sys

In = sys.stdin.readline

N = int(In())

locationList = []
answer = ''

for _ in range(N):
    location = In()[:-1].split(' ')
    locationList.append((int(location[0]), int(location[1])))

sortedList = sorted(sorted(locationList, key=lambda x: int(x[1])), key=lambda x: int(x[0]))

for data in sortedList:
    print(data[0], data[1])
