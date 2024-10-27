nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    p = 0
    d = 0
    while True:
        t = d + ((9 * (10 ** p)) * (p + 1))
        if t > n:
            break
        d = t
        p += 1

    k = int((n - d) // (p + 1)) + d
    kmod = int((n - d - 1) % (p + 1))
    #print(d, k, kmod)
    print(str(k)[kmod])





for _ in range(nm()):
    solve()
