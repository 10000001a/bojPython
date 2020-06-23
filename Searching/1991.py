import sys

In = sys.stdin.readline

N = int(In()[:-1])
treeDict = dict()
answer = [[] for _ in range(3)]

for _ in range(N):
    value, left, right = map(str, In()[:-1].split(' '))
    treeDict[value] = {
        'left': left if not left == '.' else None,
        'right': right if not right == '.' else None
    }


def preorder(node):
    answer[0].append(node)
    if treeDict[node]['left']:
        preorder(treeDict[node]['left'])
    if treeDict[node]['right']:
        preorder(treeDict[node]['right'])


def inorder(node):
    if treeDict[node]['left']:
        inorder(treeDict[node]['left'])
    answer[1].append(node)
    if treeDict[node]['right']:
        inorder(treeDict[node]['right'])


def postorder(node):
    if treeDict[node]['left']:
        postorder(treeDict[node]['left'])

    if treeDict[node]['right']:
        postorder(treeDict[node]['right'])

    answer[2].append(node)


preorder('A')
inorder('A')
postorder('A')

for i in range(3):
    x = ''
    for j in range(N):
        x += answer[i][j]
    x += '\n'
    sys.stdout.write(x)
