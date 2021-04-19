# KCY
# D2-6

k = int(input())
cnt = 0

for i in range(1, k+1):
    j = str(i)
    
    if i < 10:
        if j in ['3', '6', '9']:
            cnt = cnt + 1
            
    elif (i >= 10 and i < 100):
        for y in range(0, 2):
            if (j[y:y+1] in ['3', '6', '9']):
                cnt = cnt + 1
                
    else:
        for y in range(0, 3):
            if (j[y:y+1] in ['3', '6', '9']):
                cnt = cnt + 1
                
    if cnt > 0:
        print('-'*cnt, end = ' ')
        
    else:
        print(i, end = ' ')
        
    cnt = 0
