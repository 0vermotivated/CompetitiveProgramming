nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7


def CountToDict(x):
    sl = {}
    for i in x:
        if i not in sl:
            sl[i] = 0
        sl[i] += 1
    return sl


def solve():
    s = input()
    sl = CountToDict(s)
    c = 0
    for i in sl.values():
        if i % 2 == 1:
            c += 1
    if c > len(s) % 2:
        print("NO SOLUTION")
    else:
        save = ""
        st = ""
        for i in sl.keys():
            if sl[i] % 2 == 1:
                save = i
            st += (sl[i] // 2) * i
        print(st + save + st[::-1])





for _ in range(1):
    solve()
