N, M = map(int, input().split())
answer = 0
cardList = []

tmp = input().split()

for i in range(N):
    cardList.append(int(tmp[i]))

cardList.sort()

firstIndex = N - 3
secondIndex = N - 2
thirdIndex = N - 1

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = cardList[i] + cardList[j] + cardList[k]
            if result <= M and result > answer:
                answer = result

print(answer)

