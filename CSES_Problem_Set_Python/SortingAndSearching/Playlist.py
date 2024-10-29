import random
nm = lambda: int(input())
arri = lambda: list(map(int, input().split()))
arrs = lambda: input().split()
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    arr = arrs()
    sl = {}
    mx = 0
    cur = 0
    for i in range(n):
        k = arr[i]
        cur += 1
        if k in sl:
            cur = cur if cur < i - sl[k] else i - sl[k]
        sl[k] = i
        mx = mx if mx >= cur else cur
    print(mx)


for _ in range(1):
    solve()


