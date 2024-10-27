import sys

sys.setrecursionlimit(4 * (10 ** 4))


def go(v):
    global sl
    if v not in sl:
        return v
    if sl[v][1]:
        return v
    sl[v][1] = True
    mx = v
    for i in sl[v][0]:
        mx = max(go(i + v), mx)
    return mx


for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    l = len(lst)
    sl = {}
    v = 0
    for i in range(l):
        val = lst[i] - (l - i)
        if val not in sl:
            sl[val] = [[], False]
        sl[val][0].append(i)
    print(go(0) + l)


