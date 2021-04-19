# KCY
# D1-4-2

k = int(input())

lst = list(map(int, input().split()))

k = int((k-1)/2)
lst.sort()

print(lst[k])
