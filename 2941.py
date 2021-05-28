"Question 2941"

croatia_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
start_croatia = ["c", "d", "l", "n", "s", "z"]

str1 = input()
length = len(str1)
CNT = 0
i = 0
while i < length:
    if str1[i].isalpha() is True:
        CNT += 1
        if str1[i] in start_croatia:
            if i < length - 1:
                if str1[i] == "d":
                    if i < length -2 and str1[i + 1] == "z" and str1[i + 2] == "=":
                        i += 2
                elif str1[i] + str1[i+1] in croatia_alpha:
                    i += 1
    i += 1
print(CNT)
