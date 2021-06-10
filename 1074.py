"Question 1074"

import sys

def count_z(x, y, k, cnt):
    if k == 2:
        for i in range(x, x + k):
            for j in range(y, y + k):
                if i == r and j == c:
                    print(cnt)
                    sys.exit()
                cnt += 1
    else:
        k //= 2
        if x <= r < x + k and y <= c < y + k:
            count_z(x, y, k, cnt)
        elif x <= r < x + k and y + k <= c < y + 2 * k:
            count_z(x, y + k, k, cnt + k ** 2)
        elif x + k <= r < x + 2 * k and y <= c < y + k:
            count_z(x + k, y, k, cnt + 2 * (k ** 2))
        elif x + k <= r < x + 2 * k and y + k <= c < y + 2 * k:
            count_z(x + k, y + k, k, cnt + 3 * (k ** 2))

N, r, c = map(int, input().split())
k = 2 ** N
cnt = 0
count_z(0, 0, k, 0)
