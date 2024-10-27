nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7

def solve():
    y, x = nmm()
    if y < x:
        if x % 2 == 1:
            print((x ** 2) - y + 1)
        else:
            print((x - 1) ** 2 + y)
    elif y > x:
        if y % 2 == 0:
            print((y ** 2) - x + 1)
        else:
            print((y - 1) ** 2 + x)
    else:
        print(x ** 2 - (x - 1))




for _ in range(nm()):
    solve()