"Question 1712"

A, B, C = map(int, input().split())
if C == B or int(A / (C - B) + 1) <= 0:
    print(-1)
else:
    print(int(A / (C - B) + 1))
