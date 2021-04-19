n = list(map*(int, input().split()))

for i in range(0, len(n)):
    for j in range(i+1, len(n)):
        if (n[i] > n[j]):
            n[i], n[j] = n[j], n[i]
            
print(n)
