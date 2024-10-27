nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7


def solve():
    a, b = nmm()
    a, b = max(a, b), min(a, b)
    c = (2 * b - a)
    if c < 0:
        print("NO")
    else:
        c %= 3
        if c < 0:
            print()
        if c == 0:
            print("YES")
        else:
            print("NO")



for _ in range(nm()):
    solve()
