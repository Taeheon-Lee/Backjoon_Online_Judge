"Question 11725"

n = int(input())
tree = list([] for _ in range(n+1))

for _ in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)
    
lst = [1]
ans = {}
check = [False for _ in range(n+1)]

while len(lst) > 0:
    parent = lst.pop(0)
    for i in tree[parent]:
        if not check[i]:
            ans[i] = parent
            lst.append(i)
            check[i] = True

for i in range(2, n+1):
    print(ans[i])