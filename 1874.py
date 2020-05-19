import sys

In = sys.stdin.readline
Out = sys.stdout.write

N = int(In())

targetArray = [int(In()) for x in range(N)]

answer = ''
stack = []
element = list(range(1, N + 1))

try:
    for i in range(N):
        if len(stack) < 1:
            stack.append(element.pop(0))
            answer += '+\n'
        while targetArray[i] != stack[-1]:
            stack.append(element.pop(0))
            answer += '+\n'
        stack.pop()
        answer += '-\n'

    Out(answer)
except IndexError:
    Out('NO\n')
