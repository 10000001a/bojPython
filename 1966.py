import sys

In = sys.stdin.readline
Out = sys.stdout.write


def printerQueue():
    N, index = map(int, In().split())
    queue = list(map(int, In().split()))
    answer = 1

    for i in range(N):
        while max(queue) != queue[0]:
            queue.append(queue.pop(0))
            index = (index - 1) % N
        if index == 0:
            return answer
        queue.pop(0)
        N -= 1
        index = (index - 1) % N

        answer += 1


def main():
    testNumber = int(In())
    answer = []
    for i in range(testNumber):
        answer.append(printerQueue())
    for i in range(len(answer)):
        print(answer[i])


main()
