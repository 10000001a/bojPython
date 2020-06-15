N = int(input())

answer = 0

flyingBird = 0

while N > 0:
    flyingBird += 1
    if N < flyingBird:
        flyingBird = 1

    N -= flyingBird
    answer += 1

print(answer)