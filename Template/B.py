for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    mn = len(lst) - 1
    mx = 0
    for i in range(len(lst)):
        if lst[i] > mx:
            mx = lst[i]
            t = i
            for j in range(i + 1, len(lst)):
                if lst[j] > mx:
                    t += 1
            if t < mn:
                mn = t
    print(mn)


