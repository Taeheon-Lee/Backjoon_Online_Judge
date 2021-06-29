"Question 9997"

# passed with pypy3

def make_sentance(string, cnt, k, sign):
    global answer
    if cnt > 0:
        if sign == 1:
            answer += 1
        elif alpha == string:
            answer += 1
            sign = 1
    for i in range(k, len(lst)):
        make_sentance(string | lst[i], cnt + 1, i + 1, sign)
        cnt = 0
        sign = 0

N = int(input())
lst = []
answer = 0
alpha = (1 << 26) - 1
for _ in range(N):
    word = input()
    tmp = 0
    for elem in word:
        tmp |= 1 << (ord(elem) - ord('a'))
    lst.append(tmp)
lst = list(set(lst))
make_sentance(0, 0, 0, 0)
print(answer)