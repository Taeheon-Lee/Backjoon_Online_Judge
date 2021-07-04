"Question 1967"

import sys
sys.setrecursionlimit(10**9)

def diameter(tree, parent, ret):
    if parent not in tree.keys():
        return ret

    lst = []
    if len(tree[parent]) > 1:
        for elem in tree[parent]:
            lst.append(diameter(tree, elem[0], ret + elem[1]))
        return max(lst)
    return (diameter(tree, tree[parent][0][0], ret + tree[parent][0][1]))

n = int(input()) - 1
tree = {}
for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] in tree.keys():
        tree[tmp[0]].append([tmp[1], tmp[2]])
    else:
        tree[tmp[0]] = [[tmp[1], tmp[2]]]
answer = 0
for node in tree.keys():
    length = []
    if len(tree[node]) > 1:
        for i in range(len(tree[node])):
            length.append(diameter(tree, tree[node][i][0], tree[node][i][1]))
        length.sort(reverse=True)
        answer = max(answer, length[0] + length[1])
    else:
        answer = max(answer, diameter(tree, tree[node][0][0], tree[node][0][1]))
print(answer)