"Question 2630"

def cnt_color(frame, x, y, k):
    global cnt_white, cnt_blue
    check = frame[x][y]
    break_sign = False
    for i in range(x, x + k):
        if break_sign:
            break
        for j in range(y, y + k):
            if frame[i][j] != check:
                k //= 2
                cnt_color(frame, x, y, k)
                cnt_color(frame, x, y + k, k)
                cnt_color(frame, x + k, y, k)
                cnt_color(frame, x + k, y + k, k)
                break_sign = True
                break
    if not break_sign:
        if check == "1":
            cnt_blue += 1
        elif check == "0":
            cnt_white += 1

N = int(input())
frame = []
cnt_white = 0
cnt_blue = 0
for _ in range(N):
    tmp = list(input().split())
    frame.append(tmp)
cnt_color(frame, 0, 0, N)
print(cnt_white)
print(cnt_blue)
