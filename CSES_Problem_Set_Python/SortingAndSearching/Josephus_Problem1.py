import random
nm = lambda: int(input())
arri = lambda: list(map(int, input().split()))
arrs = lambda: input().split()
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7

def solve():
    #n = 200000
    #arr = [random.randint(-1000000, 1000000) for i in range(n)]
    n = nm()
    lst = [i + 1 for i in range(n)]
    st = 1
    while lst:
        l = len(lst)
        for i in range(st, len(lst), 2):
            print(lst[i], end=" ")
        lst = lst[abs(st - 1)::2]
        if l % 2 == 1:
            st = abs(st - 1)


for _ in range(1):
    solve()
