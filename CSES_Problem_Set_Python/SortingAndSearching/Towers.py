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
    lst = arri()
    ls2 = []
    for i in range(n):
        ls2.append([i, lst[i]])
    ls2 = sorted(ls2, key=lambda x: x[1])
    
    


for _ in range(1):
    solve()
