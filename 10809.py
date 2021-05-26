"Question 10809"

# First method

str1 = input()
answer = []
for i in range(26):
    answer.append(-1)
for i, elem in enumerate(str1):
    if answer[ord(elem) - ord('a')] == -1:
        answer[ord(elem) - ord('a')] = i
for elem in answer:
    print(elem, end=" ")
print('\n')

# Second method

answer = []
for i in range(26):
    answer.append(-1)
for elem in str1:
    answer[ord(elem) - ord('a')] = str1.index(elem)
for elem in answer:
    print(elem, end=" ")
