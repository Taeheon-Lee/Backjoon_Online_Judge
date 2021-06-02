"Question 3009"

x_lst = []
y_lst = []

for i in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

for i in range(3):
    if x_lst.count(x_lst[i]) == 1:
        tmp_x = x_lst[i]
    if y_lst.count(y_lst[i]) == 1:
        tmp_y = y_lst[i]

print(tmp_x, tmp_y)
