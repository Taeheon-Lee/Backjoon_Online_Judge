"Question 2775"

# Method 1 (Recursive)

ground=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

def resident(input_floor, input_room):
    "Counting function of resident"
    if input_room == 0:
        return 1
    if input_floor == 0:
        return ground[input_floor][n]
    ret_cnt = 0
    for i in range(input_room + 1):
        ret_cnt += resident(input_floor - 1, i)
    return ret_cnt

T = int(input())
answer = []
for i in range(T):
    k = int(input())
    n = int(input())
    if n == 1:
        answer.append(1)
    else:
        answer.append(resident(k, n - 1))

for elem in answer:
    print(elem)

# Method 2 (Make Whole Apartment)

answer = []

for i in range(T):
    k = int(input())
    n = int(input())
    if n == 1:
        answer.append(1)
        continue
    apartment = []
    for floor in range(k + 1):
        tmp = []
        for dest in range(n):
            RESIDENT = 0
            if floor == 0:
                tmp.append(dest + 1)
            else:
                for room in range(dest + 1):
                    RESIDENT = RESIDENT + apartment[floor - 1][room]
                tmp.append(RESIDENT)
        apartment.append(tmp)
    answer.append(apartment[-1][-1])

for elem in answer:
    print(elem)
