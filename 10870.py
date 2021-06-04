"Question 10870"

def fibonacci(input_num1, input_num2, cnt):
    "Fibonacci Function"
    if cnt == N:
        return input_num1
    return fibonacci(input_num2, input_num1 + input_num2, cnt + 1)

N = int(input())
print(fibonacci(0, 1, 0))
