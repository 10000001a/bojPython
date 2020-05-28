import sys

In = sys.stdin.readline
Out = sys.stdout.write

N = int(In())

targetNumbers = set(map(int, In()[:-1].split(' ')))

M = int(In())

givenNumbers = In()[:-1].split(' ')

for data in givenNumbers:
    if int(data) in targetNumbers:
        Out('1\n')
    else:
        Out('0\n')



