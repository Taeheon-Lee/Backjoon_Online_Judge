"Question 2447"

def drawing_star(N):
    if N == 1:
        return ["*"]
    
    star = []
    tmp = drawing_star(N // 3)
    for elem in tmp:
        star.append(elem * 3)
    for elem in tmp:
        star.append(elem + " " * (N // 3) + elem)
    for elem in tmp:
        star.append(elem * 3)
    return star

N = int(input())
print("\n".join(drawing_star(N)))