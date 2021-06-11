"Question 1436"

N = int(input())
now = 666
seq = 0
while 1:
    if str(now).count("666") >= 1:
        seq += 1
    if seq == N:
        print(now)
        break
    now += 1
