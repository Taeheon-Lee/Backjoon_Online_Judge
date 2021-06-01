"Question 2581"

M = int(input())
N = int(input())

eratosthenes = list(i for i in range(2, N + 1))

i = 0
while i < len(eratosthenes):
    tmp = eratosthenes[i]
    SEQ = 2
    while tmp * SEQ <= N:
        if tmp * SEQ in eratosthenes:
            eratosthenes.remove(tmp * SEQ)
        SEQ += 1
    i += 1
while len(eratosthenes) != 0 and eratosthenes[0] < M:
    eratosthenes.remove(eratosthenes[0])
if len(eratosthenes) == 0:
    print(-1)
else:
    print(sum(eratosthenes))
    print(eratosthenes[0])
