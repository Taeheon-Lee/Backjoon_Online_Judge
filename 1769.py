"Question 1769"

def trans(num, cnt):
    if len(num) == 1:
        print(cnt)
        if int(num) % 3 == 0:
            print("YES")
        else:
            print("NO")
        return
    tmp = 0
    for elem in num:
        tmp += int(elem)
    trans(str(tmp), cnt + 1)

X = input()
trans(X, 0)

# handling with number as string is faster than with number as integer