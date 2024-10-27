nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    if n == 1:
        print(1)
    elif n < 4:
        print("NO SOLUTION")
    else:
        for j in range(2, n + 1, 2):
            print(j, end=" ")
        for i in range(1, n + 1, 2):
            print(i, end=" ")


for _ in range(1):
    solve()