"Question 1662"

def unzip(Q):
    stack = []
    length = 0
    for i in range(len(Q)):
        if Q[i] == "(":
            stack.append([length-1, int(Q[i-1])])
            length = 0
        elif Q[i] == ")":
            tmp = stack.pop()
            length = (length * tmp[1] + tmp[0])
        else:
            length += 1
    return length

Q = input()
print(unzip(Q))