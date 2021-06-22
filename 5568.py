"Question 5568"

def make(cnt, num):
    if cnt == k:
        if not num in ans:
            ans.append(num)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        tmp = num
        num += card_lst[i]
        visited[i] = 1
        cnt += 1
        make(cnt, num)
        num = tmp
        visited[i] = 0
        cnt -= 1
    return

n = int(input())
k = int(input())
ans = []
card_lst = []
visited = [0] * n
for _ in range(n):
    card_lst.append(str(input()))
make(0, "")
print(len(ans))
