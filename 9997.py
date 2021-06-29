"Question 9997"

def check(string):
    tmp = [0] * 26
    for elem in string:
        tmp[ord(elem)-ord('a')] += 1
        if 0 not in tmp:
            return True
    return False

def make_sentance(string, cnt, k, sign):
    global answer
    if cnt > 0:
        if sign == 1:
            answer += 1
        elif check(string) is True:
            answer += 1
            sign = 1
    for i in range(k, len(lst)):
        back = string[:]
        string += lst[i]
        make_sentance(string, cnt + 1, i + 1, sign)
        string = back
        cnt = 0
        sign = 0

N = int(input())
lst = []
answer = 0
for _ in range(N):
    lst.append(input())
lst = list(set(lst))
make_sentance("", 0, 0, 0)
print(answer)