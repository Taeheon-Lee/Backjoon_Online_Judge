"Question 1065"

def check_hansu(input_num):
    "Check Hansu"
    tmp_n1 = input_num % 10
    input_num //= 10
    tmp_n2 = input_num % 10
    input_num //= 10
    common_diff = tmp_n2 - tmp_n1
    while input_num > 0:
        rem_dec = input_num % 10
        if rem_dec - tmp_n2 == common_diff:
            tmp_n2 = rem_dec
        else:
            return False
        input_num //= 10
    return True

X = int(input())
if X < 100:
    print(X)
else:
    CNT = 99
    for n in range(100, X + 1):
        if check_hansu(n) is True:
            CNT += 1
    print(CNT)
