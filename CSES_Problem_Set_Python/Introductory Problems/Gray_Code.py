nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def GrayCode(n):
    gc = ["0", "1"]
    for i in range(1, n):
        rgc = gc[::-1]
        gc = ["0" + i for i in gc] + ["1" + i for i in rgc]
    return gc


def solve():
    n = nm()
    res = GrayCode(n)
    for i in res:
        print(i)

for _ in range(1):
    solve()