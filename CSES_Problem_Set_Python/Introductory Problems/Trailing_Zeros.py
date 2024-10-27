nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    p = 5
    ans = 0
    while p <= n:
        ans += (n // p)
        p *= 5
    print(ans)



for _ in range(1):
    solve()