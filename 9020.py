"Question 9020"

eratosthenes = list(n for n in range(2, 10001))
for num in range(2, 5001):
    SEQ = 2
    while num * SEQ <= 10000:
        if num * SEQ in eratosthenes:
            eratosthenes.remove(num * SEQ)
        SEQ += 1

T = int(input())

for i in range(T):
    n = int(input())
    tmp = n // 2
    while 1:
        if tmp in eratosthenes:
            if n - tmp in eratosthenes:
                print(tmp, n - tmp)
                break
        tmp -= 1
