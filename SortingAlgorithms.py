def mergesort(x):
    l = len(x)
    if l < 2:
        return x
    left = mergesort(x[:l//2])
    right = mergesort(x[l//2:])
    return merge(left, right)


def merge(l, r):
    ll = len(l)
    lr = len(r)
    indl = 0
    indr = 0
    res = []
    while indr < lr and indl < ll:
        if l[indl] < r[indr]:
            res.append(l[indl])
            indl += 1
        else:
            res.append(r[indr])
            indr += 1
    for i in range(indl, ll):
        res.append(l[i])
    for i in range(indr, lr):
        res.append(r[i])
    return res





def bubblesort(x):
    l = len(x)
    for i in range(l - 1):
        for j in range(l - 1 - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


def selectionsort(x):
    l = len(x)
    for i in range(len(x)):
        mi = i
        mn = x[mi]
        for j in range(i + 1, len(x)):
            if x[j] < mn:
                mi = j
                mn = x[mi]
        x[i], x[mi] = x[mi], x[i]

    return x

