"Question 2448"

def drawing_triangle(n):
    if n == 3:
        ret = []
        ret.append("  *  ")
        ret.append(" * * ")
        ret.append("*****")
        return ret
    ret = drawing_triangle(n // 2)
    for elem in ret:
        ret.append(" " * 3 + elem)
    for i in range(n // 2):
        ret.append(ret[i] + " " + ret[i])
    return ret

tmp = (drawing_triangle(6))
for elem in tmp:
    print(elem)