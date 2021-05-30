"Question 10250"

T = int(input())
answer = []

for i in range(T):
    H, W, N = map(int, input().split())
    floor = H if N % H == 0 else N % H
    room = N // H if N % H == 0 else N // H + 1
    answer.append(floor * 100 + room)

for elem in answer:
    print(elem)
