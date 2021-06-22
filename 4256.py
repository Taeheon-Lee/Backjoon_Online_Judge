"Question 4256"

def postorder(pre_lst, in_lst):
    if len(pre_lst) == 0:
        return
    if len(pre_lst) == 1:
        print(pre_lst[0], end=" ")
        return
    key = pre_lst[0]
    for i in range(len(in_lst)):
        if in_lst[i] == key:
            loc = i
            break
    left_pre_lst = pre_lst[1:1+loc]
    right_pre_lst = pre_lst[1+loc:]
    left_in_lst = in_lst[:loc]
    right_in_lst = in_lst[loc+1:]
    postorder(left_pre_lst, left_in_lst)
    postorder(right_pre_lst, right_in_lst)
    print(key, end=" ")

T = int(input())
for _ in range(T):
    n = int(input())
    preorder_lst = list(map(int, input().split()))
    inorder_lst = list(map(int, input().split()))
    postorder(preorder_lst, inorder_lst)
    print()