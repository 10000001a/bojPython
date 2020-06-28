import sys
from collections import deque

In = sys.stdin.readline

N = int(In()[:-1])


class MinHeap:
    def __init__(self):
        self.array = deque()
        self.array.append(None)

    def insert(self, data):
        if len(self.array) == 0:
            self.array.append(None)
            self.array.append(data)

            return True

        self.array.append(data)
        inserted_index = len(self.array) - 1

        while self.is_should_move_up(inserted_index):
            parent_index = inserted_index // 2
            self.array[inserted_index], self.array[parent_index] = self.array[parent_index], self.array[inserted_index]
            inserted_index = parent_index

    def is_should_move_up(self, index):
        if index <= 1:
            return False

        if self.array[index // 2] > self.array[index]:
            return True
        else:
            return False

    def pop(self):
        if len(self.array) < 2:
            return 0
        if len(self.array) == 2:
            self.array.popleft()
            pop_elm = self.array.popleft()
            self.array.appendleft(None)

            return pop_elm

        self.array[1], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[1]

        minimum_value = self.array.pop()

        self.heap_sort()

        return minimum_value

    def heap_sort(self):
        index = 1

        while len(self.array) - 1 >= index * 2:
            if len(self.array) - 1 == index * 2:
                if self.is_should_move_up(index * 2):
                    self.array[index], self.array[index * 2] = self.array[index * 2], self.array[index]
                    index = index * 2
                else:
                    break
            else:
                left_move_up = self.is_should_move_up(index * 2)
                right_move_up = self.is_should_move_up(index * 2 + 1)
                if left_move_up and right_move_up:
                    if self.array[index * 2] <= self.array[index * 2 + 1]:
                        self.array[index], self.array[index * 2] = self.array[index * 2], self.array[index]
                        index = index * 2
                    else:
                        self.array[index], self.array[index * 2 + 1] = self.array[index * 2 + 1], self.array[index]
                        index = index * 2 + 1
                elif left_move_up:
                    self.array[index], self.array[index * 2] = self.array[index * 2], self.array[index]
                    index = index * 2
                elif right_move_up:
                    self.array[index], self.array[index * 2 + 1] = self.array[index * 2 + 1], self.array[index]
                    index = index * 2 + 1
                else:
                    break


heap = MinHeap()
answer = []
for i in range(N):
    input_value = int(In()[:-1])

    if input_value == 0:
        answer.append(heap.pop())
    else:
        heap.insert(input_value)

# sys.stdout.write(answer)
for data in answer:
    sys.stdout.write(str(answer) + '\n')
