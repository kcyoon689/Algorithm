List = [1, 3, 5, 7, 2, 4, 6]

def sequential (k):
    for i in range(len(List)):
        if List[i] == k:
            return i

print(sequential(7))

print(sequential(3))
        
