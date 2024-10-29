nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7

def solve():
    n = nm()
    arr = lst()

def solve():
    n = nm()
    arr = lst()
    arr = sorted(arr)
    k = arr[len(arr) // 2]
    c = 0
    for i in arr:
        c += abs(i - k)
    print(c)

for _ in range(1):
    solve()
