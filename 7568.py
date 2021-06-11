"Question 7568"

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])
for i in range(len(lst)):
    rank = 0
    for j in range(len(lst)):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank += 1
    print(rank + 1, end=" ")
