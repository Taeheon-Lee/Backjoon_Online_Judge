"Question 2562"

lst = []
for i in range(9):
    lst.append(int(input()))
b = max(lst)

print(b)
print(lst.index(b) + 1)
