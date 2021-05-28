"Question 1316"

def check(string):
    "check group-word"
    used = []
    i = 0
    while i < len(string):
        tmp = string[i]
        if tmp in used:
            return False
        used.append(tmp)
        while i < len(string) and string[i] == tmp:
            i += 1
    return True

N = int(input())
CNT = 0
for seq in range(N):
    input_str = input()
    if check(input_str) is True:
        CNT += 1
print(CNT)
