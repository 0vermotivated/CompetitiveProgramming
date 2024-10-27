for _ in range(int(input())):
    n = int(input())
    mh = 0
    mw = 0
    for i in range(n):
        h, w = map(int, input().split())
        mh = max(h, mh)
        mw = max(w, mw)
    print((mh + mw) * 2)
