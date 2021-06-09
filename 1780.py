"Question 1780"

def cnt_paper(x, y, k):
    "function for checking and counting each papers"
    global cnt, frame
    tmp = frame[x][y]
    check = False
    for i in range(x, x + k):
        if check is True:
            break
        for j in range(y, y + k):
            if frame[i][j] != tmp:
                k //= 3
                cnt_paper(x, y, k)
                cnt_paper(x + k, y, k)
                cnt_paper(x + k*2, y, k)
                cnt_paper(x, y + k, k)
                cnt_paper(x + k, y + k, k)
                cnt_paper(x + k*2, y + k, k)
                cnt_paper(x, y + 2*k, k)
                cnt_paper(x + k, y + 2*k, k)
                cnt_paper(x + k*2, y + 2*k, k)
                check = True
                break
    if check is False:
        cnt[int(tmp) + 1] += 1

N = int(input())
frame = []
cnt = [0, 0, 0]
for _ in range(N):
    frame.append(list(input().split()))
cnt_paper(0, 0, N)
for elem in cnt:
    print(elem)
