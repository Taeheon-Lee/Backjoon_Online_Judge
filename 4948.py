"Question 4948"

eratosthenes = list(0 for i in range(246913))
eratosthenes[0] = 1
eratosthenes[1] = 1

i = 2
while i < 246913:
    SEQ = 2
    while i * SEQ <= 246912:
        eratosthenes[i * SEQ] = 1
        SEQ += 1
    i += 1

while 1:
    n = int(input())
    if n == 0:
        break

    print(eratosthenes[n+1:2*n+1].count(0))

# Befor inputting numbers, making a cieve of Eratosthenes makes program running faster.