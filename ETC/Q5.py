def sel_sort(a):
    n = len(a)

    for i in range(0, n-1):
        k = i

        for j in range(i+1, n):
            if a[j] < a[k]:
                k = j
            a[i], a[k] = a[k], a[i]

a = list(map(int, input().split()))
sel_sort(a)

print(a)
