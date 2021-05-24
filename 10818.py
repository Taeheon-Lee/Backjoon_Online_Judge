"Question 10818"

# Using Heap

import heapq as hq

input()
lst_min = list(map(int, input().split()))
lst_max = [-x for x in lst_min]

hq.heapify(lst_min)
s = hq.heappop(lst_min)
hq.heapify(lst_max)
b = hq.heappop(lst_max) * -1

print(s, b)

# Using Built-in function

input()
lst = list(map(int, input().split()))
print(min(lst), max(lst))
