"Question 10872"

def factorial(input_num):
    "Calculating factorial"
    if input_num == 0:
        return 1
    return input_num * factorial(input_num - 1)

N = int(input())
print(factorial(N))
