"Question 2908"

n1, n2 = map(list, input().split())
n1.reverse()
n2.reverse()
if int("".join(n1)) > int("".join(n2)):
    print("".join(n1))
else:
    print("".join(n2))
