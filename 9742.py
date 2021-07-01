"Question 9742"

def permutation(lst, k):
    if k == len(lst):
        tmp.append("".join(lst))
        return
    for i in range(k, len(lst)):
        lst[k], lst[i] = lst[i], lst[k]
        permutation(lst, k+1)
        lst[k], lst[i] = lst[i], lst[k]

answer = []
while 1:
    try:
        lst, N = input().split()
        string = lst + " " + N + " = "
        tmp = []
        permutation(list(lst), 0)
        tmp.sort()
        if int(N) <= len(tmp):
            answer.append(string + tmp[int(N) - 1])
        else:
            answer.append(string + "No permutation")
    except:
        for elem in answer:
            print(elem)
        break