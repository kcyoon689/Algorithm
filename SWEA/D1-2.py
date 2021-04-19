# KCY
# D1 -2

k = int(input())

for i in range(0, k):
    j = list(map(int, input().split()))
    
    for x in range(10):
        sum += j[x]
        
    print("#%d" % (i+1), end=' ')
    print(round(sum/10))
    sum = 0
