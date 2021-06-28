"Question 2800"

def del_pren(string, k):
    global answer
    start = k
    i = k
    tmp = string[:]
    open_cnt = 0
    close_cnt = 0
    check = 0
    while i < len(tmp):
        if tmp[i] == "(":
            open_cnt += 1
            if check == 0:
                del tmp[i]
                check = 1
                start = i
                continue
        elif tmp[i] == ")":
            if open_cnt != 0:
                close_cnt += 1
            if check != 0 and open_cnt == close_cnt:
                del tmp[i]
                answer.append("".join(tmp))
                del_pren(tmp, k)
                del_pren(string, start + 1)
                break
        i += 1

input_string = list(input())
pren_lst = []
answer = []
del_pren(input_string, 0)
answer = sorted(set(answer))
for elem in answer:
    print(elem)