"Question 1002"

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if distance < max(r1, r2) - min(r1, r2):
            print(0)
        elif distance == max(r1, r2) - min(r1, r2):
            print(1)
        elif distance < r1 + r2:
            print(2)
        elif distance == r1 + r2:
            print(1)
        else:
            print(0)
