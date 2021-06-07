"Question 1991"

class Node:
    "Making Node of Tree"
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def make_tree(node_lst, num, data):
    "Making Tree"
    if data == ".":
        return None
    i = num
    while node_lst[i][0] != data:
        i += 1
    tmp = Node(node_lst[i][0])
    tmp.left = make_tree(node_lst, i, node_lst[i][1])
    tmp.right = make_tree(node_lst, i, node_lst[i][2])
    return tmp

def preorder(tree):
    "Function for preorder"
    tmp = []
    tmp += tree.data
    if tree.left != None:
        tmp += preorder(tree.left)
    if tree.right != None:
        tmp += preorder(tree.right)
    return tmp

def inorder(tree):
    "Function for inorder"
    tmp = []
    if tree.left != None:
        tmp += inorder(tree.left)
    tmp += tree.data
    if tree.right != None:
        tmp += inorder(tree.right)
    return tmp

def postorder(tree):
    "Function for postorder"
    tmp = []
    if tree.left != None:
        tmp += postorder(tree.left)
    if tree.right != None:
        tmp += postorder(tree.right)
    tmp += tree.data
    return tmp

N = int(input())
node_lst = []
for i in range(N):
    tmp = list(input().split())
    node_lst.append(tmp)
tree = make_tree(node_lst, 0, node_lst[0][0])
lst = preorder(tree)
print("".join(lst))
lst = inorder(tree)
print("".join(lst))
lst = postorder(tree)
print("".join(lst))
