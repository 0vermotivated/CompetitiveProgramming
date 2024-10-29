n, x = map(int, input().split())
arr = list(map(int, input().split()))
narr = [[i + 1, arr[i]] for i in range(n)]
narr = sorted(narr, key=lambda x: x[1])
l = 0
r = n - 1
while l < r:
    if narr[r][1] + narr[l][1] == x:
        print(narr[r][0], narr[l][0])
        break
    elif narr[r][1] + narr[l][1] > x:
        r -= 1
    else:
        l += 1
if l == r:
    print("IMPOSSIBLE")