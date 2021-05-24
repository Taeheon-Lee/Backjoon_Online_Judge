"Question 3052"

lst = []
for i in range(10):
    tmp = int(input())
    lst.append(tmp % 42)
lst = set(lst)
print(len(lst))
