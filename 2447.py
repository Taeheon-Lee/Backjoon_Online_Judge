"Question 2447"

def drawing_star(input_num):
    "function for drawing stars"
    if input_num == 1:
        return ["*"]

    star = []
    tmp = drawing_star(input_num // 3)
    for elem in tmp:
        star.append(elem * 3)
    for elem in tmp:
        star.append(elem + " " * (input_num // 3) + elem)
    for elem in tmp:
        star.append(elem * 3)
    return star

N = int(input())
print("\n".join(drawing_star(N)))
