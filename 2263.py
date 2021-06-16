"Quesion 2263"

import sys
sys.setrecursionlimit(10**9)

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    parent = post_lst[post_end]
    print(parent, end = " ")
    
    left = loc[parent] - in_start
    right = in_end - loc[parent]
    
    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)

n = int(input())
in_lst = list(map(int, input().split()))
post_lst = list(map(int, input().split()))
loc = [0] * (n + 1)
for i in range(len(in_lst)):
    loc[in_lst[i]] = i
preorder(0, n - 1, 0, n - 1)