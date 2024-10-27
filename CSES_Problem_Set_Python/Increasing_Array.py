n = int(input())
lst = list(map(int, input().split()))
mx = lst[0]
ans = 0
for i in lst:
    if i < mx:
        ans += (mx - i)
    else:
        mx = i
print(ans)