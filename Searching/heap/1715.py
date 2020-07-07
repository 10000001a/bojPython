import sys
from collections import deque

In = sys.stdin.readline

N = int(In()[:-1])


class minHeap:
    def __init__(self):
        self.heapArray = deque([])
        self.heapArray.append(None)

    def insert(self, value):
        if len(self.heapArray) == 0:
            self.heapArray.append(None)
            self.heapArray.append(value)
        else:
            self.heapArray.append(value)

        index = len(self.heapArray) - 1
        while self.is_should_up(index):
            parent_index = index // 2
            if self.heapArray[index] < self.heapArray[parent_index]:
                self.heapArray[index], self.heapArray[parent_index] \
                    = self.heapArray[parent_index], self.heapArray[index]
                index = parent_index
            else:
                break

    def is_should_up(self, index):
        parent_index = index // 2
        if index < 2:
            return False
        if self.heapArray[index] < self.heapArray[parent_index]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heapArray) == 0:

            return None
        else:
            self.heapArray[1], self.heapArray[len(self.heapArray) - 1] \
                = self.heapArray[len(self.heapArray) - 1], self.heapArray[1]
            value = self.heapArray.pop()

            self.heap_sort()

            return value

    def heap_sort(self):
        index = 1
        heapLen = len(self.heapArray)
        if heapLen < 2:
            pass
        else:
            while heapLen >= (index * 2) + 1:
                if heapLen == (index * 2) + 1:
                    if self.heapArray[index] > self.heapArray[index * 2]:
                        self.heapArray[index], self.heapArray[index * 2] \
                            = self.heapArray[index * 2], self.heapArray[index]
                        index = index * 2
                    else:
                        break
                else:
                    x = (index * 2) if self.heapArray[index * 2] < self.heapArray[index * 2 + 1] else (index * 2 + 1)
                    if self.heapArray[index] > self.heapArray[x]:
                        self.heapArray[index], self.heapArray[x] = self.heapArray[x], self.heapArray[index]
                        index = x
                    else:
                        break

    def getAnswer(self):
        answer = 0
        while len(self.heapArray) > 2:
            x = self.pop()
            y = self.pop()
            self.insert(x + y)
            answer += x + y
        return answer


minHeap = minHeap()

for _ in range(N):
    minHeap.insert(int(In()[:-1]))

print(minHeap.getAnswer())
