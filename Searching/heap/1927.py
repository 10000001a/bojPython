import heapq, sys

In = sys.stdin.readline

# answer = ""
N = int(In()[:-1])
answer2 = []

minHeap = []

for _ in range(N):
    x = int(In()[:-1])

    if x == 0:
        if minHeap:
            # answer += str(heapq.heappop(minHeap)) + '\n'
            answer2.append(heapq.heappop(minHeap))
        else:
            # answer += '0\n'
            answer2.append(0)
    else:
        heapq.heappush(minHeap, x)

for data in answer2:
    print(data)
# sys.stdout.write(answer2)
