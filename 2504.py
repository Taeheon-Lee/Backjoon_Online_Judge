"Question 2504"

import sys

exp = input()
stack = []
for elem in exp:
    if elem in ("(", "["):
        stack.append(elem)
    elif elem in (")", "]"):
        tmp = elem
        num = 0
        while stack:
            sign = stack.pop()
            if sign.isdigit():
                num = num + int(sign)
            elif (sign == "(" and tmp == ")") or (sign == "[" and tmp == "]"):
                if num == 0 and sign == "(":
                    stack.append("2")
                    break
                if num == 0 and sign == "[":
                    stack.append("3")
                    break
                if sign == "(":
                    stack.append(str(num * 2))
                    break
                if sign == "[":
                    stack.append(str(num * 3))
                    break
            else:
                print(0)
                sys.exit()
    else:
        print(0)
        sys.exit()
ans = 0
for elem in stack:
    if elem.isdigit() is False:
        print(0)
        sys.exit()
    else:
        ans += int(elem)
print(ans)
