"Question 10829"

def binary(N, bi_str):
    if N == 0:
        return bi_str
    bi_str = binary(N // 2, bi_str) + str(N % 2)
    return bi_str

N = int(input())
print(binary(N, ""))