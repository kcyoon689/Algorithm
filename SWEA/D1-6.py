# KCY
# D1-6

k = int(input())
sum = 0

for i in range(0, 4):
    if k <= 0:
        break;
    
    j = k % 10
    k = int(k / 10)
    sum = sum + j
    
print(sum)
