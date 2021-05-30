"Question 1193"

X = int(input())
START = 0
END = 1
CNT = 1
while 1:
    if START < X <= END:
        if CNT % 2 != 0:
            print(CNT + 1 - (X - START), "/", X - START, sep="")
        else:
            print(X - START, "/",  CNT + 1 - (X - START), sep="")
        break
    CNT += 1
    START = END
    END = END + CNT
