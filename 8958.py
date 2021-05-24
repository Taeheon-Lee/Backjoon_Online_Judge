"Question 8958"

q = int(input())
answer = []
for i in range(q):
    SCORE = 0
    TMP = 0
    s = input()
    for elem in s:
        if elem == "O":
            TMP += 1
        else:
            TMP = 0
        SCORE += TMP
    answer.append(SCORE)
for elem in answer:
    print(elem)
