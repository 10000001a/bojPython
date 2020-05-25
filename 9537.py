import sys

In = sys.stdin.readline
Out = sys.stdout.write


def getGCD(a, b):
    if a < b:
        (a, b) = (b, a)
    if a == b:
        return a
    while b != 0:
        (a, b) = (b, a % b)
    return a


def getAnswer():
    length = int(In())
    array = list(map(int, In().split()))
    answer = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            tmp = getGCD(array[i], array[i + 1])
            for k in range(i+2, j+1):
                tmp = getGCD(tmp, array[k])
            if tmp * (j - i + 1) > answer:
                answer = tmp * (j - i + 1)

    return answer


def main():
    testNumber = int(In())
    answer = ''
    for i in range(testNumber):
        answer += str(getAnswer()) + '\n'
    Out(answer)


main()
