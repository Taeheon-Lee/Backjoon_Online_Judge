"Question 2292"

N = int(input())
START = 0
END = 1
CNT = 0
while 1:
    CNT += 1
    if START < N <= END:
        print(CNT)
        break
    START = END
    END = END + 6 * CNT
