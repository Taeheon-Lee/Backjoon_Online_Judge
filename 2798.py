"Question 2798"

N, M = map(int, input().split())
lst = list(map(int, input().split()))
diff = 1000000000

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = M - (lst[i] + lst[j] + lst[k])
            if 0 <= tmp < diff:
                diff = tmp
                answer = lst[i] + lst[j] + lst[k]
print(answer)
