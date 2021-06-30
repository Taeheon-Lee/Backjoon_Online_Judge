"Question 16505"

def drawing_star(N):
    if N == 0:
        return "*"
    lst = []
    tmp = drawing_star(N-1)
    for i in range(len(tmp)):
        lst.append(tmp[i] + " " * i + tmp[i])
    for i in range(len(tmp)):
        lst.append(tmp[i])
    return lst

N = int(input())
answer = drawing_star(N)
for elem in answer:
    print(elem)