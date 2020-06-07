import sys

In = sys.stdin.readline
Out = sys.stdout.write

testNumber = int(In()[:-1])
answer = [[] for _ in range(testNumber)]


def evaluate(string):
    return eval(string.replace(' ', ''))


def findZero(exp, num, N, caseNumber):
    if num != N:
        findZero(exp + '+' + str(num + 1), num + 1, N, caseNumber)
        findZero(exp + '-' + str(num + 1), num + 1, N, caseNumber)
        findZero(exp + ' ' + str(num + 1), num + 1, N, caseNumber)
    else:
        if evaluate(exp) == 0:
            global answer
            answer[caseNumber].append(exp)


for i in range(testNumber):
    N = int(In()[:-1])
    findZero('1', 1, N, i)
    answer[i].sort()

for data1 in answer:
    for data2 in data1:
        Out(data2+'\n')
    Out('\n')
