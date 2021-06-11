"Question 1018"

def recolor(frame, row, col):
    start_w = 0
    start_b = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if (i - row) % 2 == 0 and (j - col) % 2 == 0:
                if frame[i][j] != "W":
                    start_w += 1
                else:
                    start_b += 1
            elif (i - row) % 2 == 0 and (j - col) % 2 == 1:
                if frame[i][j] != "B":
                    start_w += 1
                else:
                    start_b += 1
            elif (i - row) % 2 == 1 and (j - col) % 2 == 0:
                if frame[i][j] != "B":
                    start_w += 1
                else:
                    start_b += 1
            else:
                if frame[i][j] != "W":
                    start_w += 1
                else:
                    start_b += 1
    return start_w if start_w < start_b else start_b

N, M = map(int, input().split())
ret = 100000000000
frame = []
for _ in range(N):
    frame.append(input())
for i in range(N - 7):
    for j in range(M - 7):
        tmp = recolor(frame, i, j)
        if ret > tmp:
            ret = tmp
print(ret)