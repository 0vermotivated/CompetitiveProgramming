n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
l = 0
r = n - 1
c = 0
while l < r:
    if arr[l] + arr[r] <= k:
        l += 1
        r -= 1
        c += 1
    else:
        r -= 1
        c += 1
if l == r:
    c += 1
print(c)
