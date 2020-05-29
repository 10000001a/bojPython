import sys

In = sys.stdin.readline

N = int(In())

userList = []
answer = ''

for i in range(N):
    a = In()[:-1].split(' ')

    userList.append(tuple([int(a[0]), a[1]]))

sortedList = sorted(userList, key=lambda x: x[0])

for tupleData in sortedList:
    print(tupleData[0], tupleData[1])
