# KCY
# D1-12

k = int(input())

for i in range(0, k):
    a, b = map(int, input().split())
    
    print("#%d" % (i+1), end=' ')
    print(int(a/b), a%b)
