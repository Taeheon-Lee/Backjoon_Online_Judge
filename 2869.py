"Question 2869"

A, B, V = map(int, input().split())

V = V - A
if V % (A - B) == 0:
    print(V // (A - B) + 1)
else:
    print(V // (A - B) + 2)
