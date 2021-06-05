"Question 11729"

def hanoi(num, start, end, middle, tmp):
    "function for moving process of Hanoi"
    if num == 1:
        tmp.append([start, end])
        return tmp
    hanoi(num - 1, start, middle, end, tmp)
    tmp.append([start, end])
    hanoi(num - 1, middle, end, start, tmp)
    return tmp

N = int(input())
answer = []
answer = hanoi(N, 1, 3, 2, answer)
print(len(answer))
for elem in answer:
    print(elem[0], elem[1])
