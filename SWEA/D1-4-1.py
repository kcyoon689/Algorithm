# KCY
# D1-4-1

k = int(input())

for i in range(k):
    j = list(map(int, input().split()))
    j.sort()
    
    print("#%d" %(i+1), j[9])
