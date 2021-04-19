# KCY
# D2-5

k = int(input())

for i in range(1, k+1):
    s = input()
    
    if s == s[::-1]:
        print("#%d" %i, 1)
        
    else:
        print("#%d" %i, 0)
