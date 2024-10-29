def CoinGreedy(ts, noms): #not always correct
    noms = sorted(noms)
    l = len(noms)
    r = []
    for i in range(l - 1, -1, -1):
        c = noms[i]
        cnt = ts // c
        ts -= (c * cnt)
        r.append([c, cnt])
    if ts != 0:
        return False
    else:
        return r

'''
n = [1, 5, 10, 43, 81, 32, 64]
k = 5783
print(CoinGreedy(k, n))
'''





