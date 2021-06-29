"Question 9997"

def check(string):
    tmp = [0] * 26
    for elem in string:
        tmp[ord(elem)-ord('a')] += 1
    if 0 not in tmp:
        return True
    return False

def make_sentance(string, cnt, k):
    global answer
    if cnt > 0:
        if check(string) is True:
            answer += 1
    back = string[:]
    for i in range(k, len(lst)):
        string += lst[i]
        make_sentance(string, cnt + 1, k + 1)
        make_sentance(back, 0, i)
        

N = int(input())
lst = []
answer = 0
for _ in range(N):
    lst.append(input())
lst = list(set(lst))
make_sentance("", 0, 0)