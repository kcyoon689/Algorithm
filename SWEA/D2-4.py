# KCY
# D2-4

k = int(input())
for i in range(1, k+1):
    n = int(input())
    sum = 0
    for j in range(1, n+1):
        if j % 2== 0:
            sum = sum - j
        else:
            sum = sum + j
    print("#%d" %i, sum)
