"Question 2231"

def cal(num):
    ret = num
    while num != 0:
        ret += num % 10
        num //= 10
    return ret

N = int(input())
if N < 10:
    print(0)
else:
    for i in range(1, N + 1):
        if cal(i) == N:
            print(i)
            break
        if i == N:
            print(0)
