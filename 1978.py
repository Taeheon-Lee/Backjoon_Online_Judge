"Question 1978"

eratosthenes = list(i for i in range(2, 1001))

i = 0
while i < len(eratosthenes):
    tmp = eratosthenes[i]
    SEQ = 2
    while tmp * SEQ <= 1000:
        if tmp * SEQ in eratosthenes:
            eratosthenes.remove(tmp * SEQ)
        SEQ += 1
    i += 1

input()
lst = list(map(int, input().split()))
CNT = 0
for elem in lst:
    if elem in eratosthenes:
        CNT += 1
print(CNT)
