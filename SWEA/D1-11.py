# KCY
# D1-11

a, b = map(int, input().split())
cnt = 1

while(1):
    if a == b:
        print(cnt)
        break
    
    b = b + 1
    cnt = cnt + 1
