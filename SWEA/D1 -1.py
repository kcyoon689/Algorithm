# KCY
# D1 -1

k = int(input())
for i in range(k):
    j = list(map(int, input().split()))
    sum_num = 0
    for y in range(len(j)):
        if j[y] % 2 != 0:
            sum_num = sum_num + j[y]
        else:
            continue
    print("#%d" %(i+1), sum_num)
