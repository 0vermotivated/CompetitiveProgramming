def BestSubstringSum(arr):
    l = len(arr)
    bind = [0, 0]
    ind = [0, 0]
    best, s = 0, 0
    for i in range(l):
        if arr[i] > s + arr[i]:
            s = arr[i]
            ind = [i, i + 1]
        else:
            s += arr[i]
            ind[1] += 1
        if best < s:
            best = s
            bind = ind.copy()
    return best, bind
