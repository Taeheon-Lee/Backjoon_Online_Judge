"Question 4344"

n_class = int(input())
answer = []
for i in range(n_class):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0]
    CNT = 0
    for elem in lst[1:]:
        if elem > avg:
            CNT += 1
    answer.append(CNT / lst[0] * 100)
for elem in answer:
    print("%0.3f%%" % elem)
