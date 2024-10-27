nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nms = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    if n % 4 in (1, 2):
        print("NO")
    else:
        print("YES")
        if n % 2:
            l1 = []
            l2 = []
            for i in range(1, n + 1):
                if i % 4 in (1, 2):
                    l1.append(i)
                else:
                    l2.append(i)
        else:
            l1 = []
            l2 = []
            for i in range(1, n + 1):
                if i % 4 in (2, 3):
                    l1.append(i)
                else:
                    l2.append(i)
        print(len(l1))
        print(*l1)
        print(len(l2))
        print(*l2)


for _ in range(1):
    solve()