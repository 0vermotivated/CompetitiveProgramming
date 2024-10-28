import sys
def lst(): return list(map(int, sys.stdin.readline().strip().split()))
def st(): return sys.stdin.readline().strip()
nm = lambda: int(input())
nmm = lambda: map(int, input().split())
MOD = 10 ** 9 + 7


def solve():
    n = nm()
    print(len(set(lst())))


for _ in range(1):
    solve()