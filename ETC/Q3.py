n = list(map*(int, input().split()))

ans = 0

for i in n:
    ans += i # 원소 값을 하나씩 받아서 ans에 덧셈

print(ans)
