"Question 1157"

str1 = input().upper()
answer = []
for i in range(26):
    answer.append(0)
for elem in str1:
    answer[ord(elem)-ord('A')] += 1
if answer.count(max(answer)) > 1:
    print('?')
else:
    print(chr(answer.index(max(answer))+ord('A')))
