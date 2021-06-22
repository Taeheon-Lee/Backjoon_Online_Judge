"Question 16198"

def energe(lst, n):
    if len(lst) == 3:
        return lst[0] * lst[-1]
    for i in range(1, len(lst)):
        energe(lst, i)
    return lst

input()
lst = list(map(int, input().split()))
print(energe(lst, 0))