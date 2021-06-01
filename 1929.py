"Question 1929"

# import time

# method 1 (Using check function)

M, N = map(int, input().split())

# start = time.time()

def check(input_num):
    "A fuction for checking a prime number"
    if input_num == 1:
        return False
    for i in range(2, int(input_num ** 0.5) + 1):
        if input_num % i == 0:
            return False
    return True

for num in range(M, N + 1):
    if check(num) is True:
        print(num)

# end = time.time()
# print("실행 시간 :", end - start)

# method 2 (Using Eratosthenes)

M, N = map(int, input().split())

# start = time.time()

eratosthenes = list(0 for i in range(N+1))

i = 2
while i < N+1:
    SEQ = 2
    while i * SEQ <= N:
        eratosthenes[i * SEQ] = 1
        SEQ += 1
    i += 1

i = M
while i <= N:
    if i == 1:
        pass
    if eratosthenes[i] == 0:
        print(i)
    i += 1

# end = time.time()
# print("실행 시간 :", end - start)

# Comparing both 2 algoritms, the method 1 is later than method 2.
# But method 1 is faster about time of starting time of printing.
