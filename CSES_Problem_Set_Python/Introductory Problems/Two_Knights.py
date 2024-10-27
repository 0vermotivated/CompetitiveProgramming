nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    for i in range(1, n + 1):
        tot = i ** 2
        ways = (tot * (tot - 1)) // 2
        if i > 2:
            ways -= 4 * (i - 1) * (i - 2)
        print(ways)


for _ in range(1):
    solve()