import sys

N = int(sys.stdin.readline()[:-1])

fibArray = [0 for _ in range(46)]
fibArray[1] = 1
fibArray[2] = 1


def fib(N):
    if N == 0:
        return 0
    if fibArray[N] != 0:
        return fibArray[N]
    fibArray[N] = fib(N - 1) + fib(N - 2)
    return fibArray[N]


sys.stdout.write(str(fib(N)) + '\n')
