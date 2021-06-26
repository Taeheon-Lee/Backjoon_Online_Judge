def moo(length, K, N):
    middle = (length - (K + 3)) / 2 + 1
    if N == middle:
        print("m")
        return
    if middle < N <= middle + K + 2:
        print("o")
        return
    if N < middle:
        moo((length - (K + 3)) / 2, K - 1, N)
    elif N > middle + K + 2:
        moo(middle - 1, K - 1, N - (middle - 1 + K + 3))

N = int(input())
K = 0
length = 3
while 1:
    if length > N:
        break
    K += 1   
    length = 2 * length + K + 3
moo(length, K, N)