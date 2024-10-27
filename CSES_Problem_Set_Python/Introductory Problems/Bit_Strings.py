nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7


def solve():
    print(2 ** nm() % MOD)


for _ in range(1):
    solve()
