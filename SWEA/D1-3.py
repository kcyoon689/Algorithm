# KCY
# D1-3

k = int(input())
for i in range(0, k):
    a, b = map(int, input().split())
    print("#%d" % (i+1), end=' ')
    
    if a < b:
        print("<")
    elif a == b:
        print("=")
    else:
        print(">")
