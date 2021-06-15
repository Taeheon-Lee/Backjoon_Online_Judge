"Question 5639"

import sys
sys.setrecursionlimit(10**9)

def postorder(start, end):
    if start > end:
        return
    
    division = end
    for i in range(start + 1, end + 1):
        if node_lst[start] < node_lst[i]:
            division = i - 1
            break
    postorder(start + 1, division)
    postorder(division + 1, end)
    print(node_lst[start])

node_lst = []
while 1:
    try:
        node_lst.append(int(input()))
    except:
        break
postorder(0, len(node_lst) - 1)
