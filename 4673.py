"Question 4673"

lst = []
for n in range(10000):
    lst.append(0)

def check_lst(start_num):
    "count self number"
    tmp = start_num
    while start_num != 0:
        tmp = tmp + start_num % 10
        start_num //= 10
    if tmp > 10000:
        return
    lst[tmp-1] += 1
    check_lst(tmp)

i = 0
for i in range(1, 10001):
    check_lst(i)
for i in range(10000):
    if lst[i] == 0:
        print(i + 1)
