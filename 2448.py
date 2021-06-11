"Question 2448"

def drawing_triangle(n):
    if n == 3:
        ret = []
        ret.append("  *  ")
        ret.append(" * * ")
        ret.append("*****")
        return ret
    tmp = drawing_triangle(n // 2)
    ret = []
    for elem in tmp:
        ret.append(" " * (n // 2) + elem + " " * (n // 2))
    for elem in tmp:
        ret.append(elem + " " + elem)
    return ret

N = int(input())
tmp = (drawing_triangle(N))
for elem in tmp:
    print(elem)
