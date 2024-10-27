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
    mx = l
    q = [0]
    while q:
        nxt = q.pop()
        if nxt in sl:
            if not sl[nxt][1]:
                sl[nxt][1] = True
                for i in sl[nxt][0]:
                    q.append(i + nxt)
        else:
            mx = max(mx, nxt + l)
    print(mx)