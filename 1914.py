"Question 1914, same as 11729 with limit of memory"

def Hanoi(num, start, middle, end):
    if num == 1:
        print(start, end)
        return
    
    Hanoi(num - 1, start, end, middle)
    print(start, end)
    Hanoi(num - 1, middle, start, end)
    return

N = int(input())
print(2 ** N - 1)
if N <= 20:
    Hanoi(N, 1, 2, 3)
