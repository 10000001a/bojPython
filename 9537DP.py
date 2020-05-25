import collections
import sys

In = sys.stdin.readline
Out = sys.stdout.write


def getGCD(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def getAnswer():
    length = int(In())
    print(length)
    array = list(map(int, In().split()))
    array = collections.deque(map(int, In().split()))
    print(array)
    answer = 0
    for i in range(length - 1):
        dp = [None for i in range(length)]
        for j in range(i + 1, length):
            if answer // (j - i + 1) < array[i] and answer // (j - i + 1) < array[j]:
                if dp[j - 1] is None:
                    dp[j] = getGCD(array[i], array[j])
                else:
                    dp[j] = getGCD(dp[j-1], array[j])

                if dp[j] * (j - i + 1) > answer:
                    answer = dp[j] * (j - i + 1)
    #
    # for i in range(length - 1):
    #     for j in range(i + 1, length):
    #         if not dp[i][j] is None:
    #             handsomeGCD = dp[i][j] * (j - i + 1)
    #             if handsomeGCD > answer:
    #                 answer = handsomeGCD
    return answer


def main():
    testNumber = int(In())
    answer = ''
    for i in range(testNumber):
        print(i)
        answer += str(getAnswer()) + '\n'
    Out(answer)


main()
