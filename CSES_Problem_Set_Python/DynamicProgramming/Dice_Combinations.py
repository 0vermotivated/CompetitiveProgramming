import random
nm = lambda: int(input())
arri = lambda: list(map(int, input().split()))
arrs = lambda: input().split()
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7
INF = (2 ** 64) + 1

def solve():
    n = nm()
    lst = [0 for i in range(10 ** 6 + 1)]
    lst[0] = 1
    lst[1] = 1
    lst[2] = 2
    lst[3] = 4
    lst[4] = 8
    lst[5] = 16
    for i in range(6, 10 ** 6 + 1):
        lst[i] = (sum(lst[i - 6:i])) % MOD
    print(lst[n])


for _ in range(1):
    solve()
