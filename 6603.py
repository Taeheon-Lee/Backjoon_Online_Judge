"Question 6603"

def lotto(i, cnt):
    "Lotto"
    if cnt == 6:
        for j in range(len(visited)):
            if visited[j] == 1:
                print(S[j], end=" ")
        print()

    for j in range(i, k):
        visited[j] = 1
        lotto(j + 1, cnt + 1)
        visited[j] = 0

while 1:
    tmp = list(map(int, input().split()))
    k = tmp[0]
    if k == 0:
        break
    S = tmp[1:]
    visited = [0] * k
    lotto(0, 0)
    print()
