"Question 10994"

def drawing(N):
    if N == 1:
        return ["*"]
    tmp = drawing(N - 1)
    lst = []
    length = len(tmp[0])
    lst.append(tmp[0] + "*" * 4)
    lst.append("*" + " " * (length + 2) + "*")
    for elem in tmp:
        lst.append("* " + elem + " *")
    lst.append("*" + " " * (length + 2) + "*")
    lst.append(tmp[0] + "*" * 4)
    return lst

N = int(input())
answer = drawing(N)
for elem in answer:
    print(elem)