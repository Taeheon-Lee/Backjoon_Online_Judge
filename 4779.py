"Question 4779"

def cantor(lst, num, end):
    if num == end:
        return lst
    lst = lst + " " * len(lst) + lst
    return cantor(lst, num + 1, end)

answer = []
while 1:
    try:
        N = int(input())
        answer.append(cantor("-", 0, N))
    except:
        for elem in answer:
            print(elem)
        break