import sys

In = sys.stdin.readline

N, r, c = map(int, In()[:-1].split(' '))


def getQuadrant(n, r, c):
    if r // (2 ** (n - 1)) == 0:
        if c // (2 ** (n - 1)) == 0:
            return 1
        else:
            return 2
    else:
        if c // (2 ** (n - 1)) == 0:
            return 3
        else:
            return 4


def getAnswer(n, r, c):
    quadrantNumber = getQuadrant(n, r, c)
    c = c % (2 ** (n - 1))
    r = r % (2 ** (n - 1))

    if n > 0:
        return ((2 ** (2 * (n - 1))) * (quadrantNumber - 1)) + getAnswer(n - 1, r, c)
    else:
        return 0


print(getAnswer(N, r, c))
