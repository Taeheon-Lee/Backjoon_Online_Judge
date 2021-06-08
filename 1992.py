"Question 1992"

def check(frame):
    "check condition"
    tmp = frame[0][0]
    for arr in frame:
        for elem in arr:
            if elem != tmp:
                return False
    return tmp

def compress(frame, length):
    "function for compress"
    tmp = check(frame)
    if tmp is not False:
        return tmp
    res = ""
    sec1 = []
    sec2 = []
    sec3 = []
    sec4 = []
    for i in range(length // 2):
        tmp = []
        for j in range(length // 2):
            tmp.append(frame[i][j])
        sec1.append(tmp)
    for i in range(length // 2):
        tmp = []
        for j in range(length // 2, length):
            tmp.append(frame[i][j])
        sec2.append(tmp)
    for i in range(length // 2, length):
        tmp = []
        for j in range(length // 2):
            tmp.append(frame[i][j])
        sec3.append(tmp)
    for i in range(length // 2, length):
        tmp = []
        for j in range(length // 2, length):
            tmp.append(frame[i][j])
        sec4.append(tmp)
    lst = [sec1, sec2, sec3, sec4]
    for i in range(4):
        lst[i] = compress(lst[i], length // 2)
        if len(lst[i]) == 1:
            res += lst[i]
        else:
            res = res + "(" + "".join(lst[i]) + ")"
    return res

N = int(input())
frame = []
for _ in range(N):
    frame.append(list(input()))
if check(frame) is False:
    print("(" + compress(frame, N) + ")")
else:
    print(check(frame))
