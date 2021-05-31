"Question 1011"

T = int(input())
answer = []

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    if distance in (1, 2, 3):
        answer.append(distance)
    else:
        CNT = 3
        tmp = distance ** (1 / 2)
        if tmp - int(tmp) != 0:
            tmp = int(distance ** (1 / 2)) + 1
        else:
            tmp = int(distance ** (1 / 2))
        if (tmp - 1) ** 2 + tmp < distance:
            CNT = CNT + 2 * (tmp - 2)
        else:
            CNT = CNT + 2 * (tmp - 2) - 1
        answer.append(CNT)

for elem in answer:
    print(elem)
