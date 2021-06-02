"Question 4153"

while 1:
    n1, n2, n3 = map(int, input().split())
    if n1 == 0 and n2 == 0 and n3 == 0:
        break

    lst = [n1, n2, n3]
    lst.sort()
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print("right")
    else:
        print("wrong")
