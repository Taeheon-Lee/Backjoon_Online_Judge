"Question 16198"

def collect(energe):
    global ans
    if (len(lst) == 2):
        ans = max(ans, energe)
        return
    else:
        for i in range(1, len(lst) - 1):
            tmp_energe = lst[i - 1] * lst[i + 1]
            tmp_loc = lst[i]
            del lst[i]
            collect(energe + tmp_energe)
            lst.insert(i, tmp_loc)
    
input()
lst = list(map(int, input().split()))
ans = 0
collect(0)
print(ans)