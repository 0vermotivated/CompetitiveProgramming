nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7

def solve():
    n = int(input())
    arr = lst()
    narr = []
    for i in range(n):
        narr.append([i, arr[i]])
    narr = sorted(narr, key=lambda x: x[1])
    c = 1
    p = -1
    for i in narr:
        if i[0] < p:
            c += 1
        p = i[0]
    print(c)


for _ in range(1):
    solve()
