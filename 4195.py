import sys

In = sys.stdin.readline
Out = sys.stdout.write

testNumber = int(In())
answer = ''


def findParent(x):
    if parentTable[x] == x:
        return x
    else:
        tmp = findParent(parentTable[x])
        parentTable[x] = tmp
        return tmp


def union(x, y):
    x = findParent(x)
    y = findParent(y)

    if x != y:
        parentTable[y] = x
        sizeTable[x] += sizeTable[y]
        return str(sizeTable[x]) + '\n'

    return str(sizeTable[x]) + '\n'


for x in range(testNumber):
    parentTable = dict()
    sizeTable = dict()
    relationNumber = int(In())
    for _ in range(relationNumber):
        friendA, friendB = In()[:-1].split(' ')

        if friendA not in parentTable:
            parentTable[friendA] = friendA
            sizeTable[friendA] = 1

        if friendB not in parentTable:
            parentTable[friendB] = friendB
            sizeTable[friendB] = 1

        answer += union(friendA, friendB)

Out(answer)
