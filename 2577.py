"Question 2577"

ANSWER = 1
for i in range(3):
    tmp = int(input())
    ANSWER = ANSWER * tmp

ANSWER = str(ANSWER)
for i in range(10):
    i = str(i)
    print(ANSWER.count(i))
