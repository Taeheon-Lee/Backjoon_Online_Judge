"Question 10993"

def drawing(N):
    if N == 1:
        return ["*"]
    ret = []
    tmp = drawing(N-1)
    if N % 2 == 0:
        start = tmp[-1]
        plus_length = len(tmp)
        cnt = len(start) - 2
        for i in range(len(tmp) * 2 + 1):
            if i == 0:
                ret += [2 * "*" * (plus_length + 1) + start]
            elif 0 < i < len(tmp) + 1:
                ret += [" " * i + "*" + " " * (plus_length - i) + tmp[i - 1] + " " * (plus_length - i) + "*" + " " * i]
            elif len(tmp) < i < len(tmp) * 2:
                ret += [" " * i + "*" + " " * cnt + "*" + " " * i]
                cnt -= 2
            else:
                ret += [" " * i + "*" + " " * i]
    else:
        start = tmp[0]
        plus_length = len(tmp)
        cnt = 1
        for i in range(len(tmp) * 2, -1, -1):
            if i == len(tmp) * 2:
                ret += [" " * i + "*" + " " * i]
            elif len(tmp) < i < len(tmp) * 2:
                ret += [" " * i + "*" + " " * cnt + "*" + " " * i]
                cnt += 2
            elif 0 < i < len(tmp) + 1:
                ret += [" " * i + "*" + " " * (plus_length - i) + tmp[len(tmp) - i] + " " * (plus_length - i) + "*" + " " * i]
            else:
                ret += [2 * "*" * (plus_length + 1) + start]
    return ret

N = int(input())
answer = drawing(N)
for elem in answer:
    print(elem)