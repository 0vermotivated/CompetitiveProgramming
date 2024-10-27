nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

'''
def solve():
    n = nm()
    ar = lst()
    s = sum(ar)
    dp = [False for i in range(s // 2 + 1)]
    dp[0] = True
    for i in ar:
        for j in range((s // 2) - i, -1, -1):
            if dp[j]:
                dp[j + i] = True
    for i in range(len(dp) -1, -1, -1):
        if dp[i]:
            print(abs(s - (2 * i)))
            break

'''

def solve():
    n = nm()
    ar = lst()
    s = sum(ar)
    dp = {0}
    for i in ar:
        dp2 = dp.copy()
        for j in dp:
            if j + i <= (s // 2) + (s % 2):
                dp2.add(j + i)
        dp = dp2.copy()
    k = max(dp)
    print(abs(2 * k - s))




for _ in range(1):
    solve()
