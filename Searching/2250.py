import sys

In = sys.stdin.readline

N = int(In()[:-1])

maxColumn = dict()
minColumn = dict()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = 0
        self.column = 0

    def setChild(self, left, right):
        if left is not None:
            self.left = left

        if right is not None:
            self.right = right

    def setLevel(self, level):
        self.level = level

    def setColumn(self, column):
        self.column = column

    def countNodes(self):
        count = 0
        if self.left:
            count += self.left.countNodes()
        count += 1
        if self.right:
            count += self.right.countNodes()

        return count

    def countLeftSubTree(self):
        if self.left:
            return self.left.countNodes()
        else:
            return 0

    def countRightSubTree(self):
        if self.right:
            return self.right.countNodes()
        else:
            return 0


NodeArray = [Node(i) for i in range(N + 1)]

for _ in range(N):
    i, left, right = map(int, list(In()[:-1].split(' ')))
    if left == -1:
        left = None
    else:
        left = NodeArray[left]
    if right == -1:
        right = None
    else:
        right = NodeArray[right]
    NodeArray[i].setChild(left, right)

parent = True
root = 1
while parent:
    parent = False
    for node in NodeArray:
        if node.left:
            if node.left.value == root:
                root = node.value
                parent = True
                break
        if node.right:
            if node.right.value == root:
                root = node.value
                parent = True
                break


def setNodesAttribute(node, start, level):  # start = 1
    node.setLevel(level)
    column = start + node.countLeftSubTree()
    node.setColumn(column)
    if node.left:
        setNodesAttribute(node.left, start, level + 1)
    if node.right:
        setNodesAttribute(node.right, column + 1, level + 1)


setNodesAttribute(NodeArray[root], 1, 1)

for data in NodeArray:
    if data.level not in maxColumn:
        maxColumn[data.level] = data.column
    else:
        if maxColumn[data.level] < data.column:
            maxColumn[data.level] = data.column

    if data.level not in minColumn:
        minColumn[data.level] = data.column
    else:
        if minColumn[data.level] > data.column:
            minColumn[data.level] = data.column

gap = [(maxColumn[i] - minColumn[i] + 1) for i in range(len(minColumn))]
gap[0] = 0

answer = max(gap)
index = gap.index(answer)
print(index, answer)
