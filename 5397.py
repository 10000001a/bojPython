import sys
from collections import deque

In = sys.stdin.readline
Out = sys.stdout.write


def keyLogger():
    string = deque(In())
    beforeCursor = deque('')
    afterCursor = deque('')

    for ch in string:
        if ch == '<':
            if not len(beforeCursor) == 0:
                afterCursor.appendleft(beforeCursor.pop())
        elif ch == '>':
            if not len(afterCursor) == 0:
                beforeCursor.append(afterCursor.popleft())
        elif ch == '-':
            if not len(beforeCursor) == 0:
                beforeCursor.pop()
        elif ch == '\n':
            beforeCursor.extend(afterCursor)

            return ''.join(beforeCursor) + '\n'
        else:
            beforeCursor.append(ch)


def main():
    testNumber = int(In())
    answer = ''

    for _ in range(testNumber):
        answer += keyLogger()

    Out(answer)


main()
