"Question 2839"

N = int(input())

CNT = 0
while 1:
    if N % 5 != 0:
        if  N < 3:
            CNT = -1
            break
        N -= 3
        CNT += 1
    else:
        CNT += N // 5
        break
print(CNT)
