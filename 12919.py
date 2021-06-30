"Question 12919"

def matching(lst):
    if len(lst) != len(dest):
        pass
    elif lst == dest:
        return 1
    else:
        return 0
    if lst[-1] == "A":
        if matching(lst[:-1]) == 1:
            return 1
    if lst[0] == "B":
        lst = lst[1:]
        if matching(lst[::-1]) == 1:
            return 1
    return 0

dest = input()
start = input()
print(matching(start))