MOD = 10 ** 9 + 7


def CountToDict(x):
    sl = {}
    for i in x:
        if i not in sl:
            sl[i] = 0
        sl[i] += 1
    return sl

'''
A Gray code is a list
of all 2^n bit strings of length n,
where any two successive strings differ in 
exactly one bit (i.e., their Hamming distance is one).
'''
def GrayCode(n):
    gc = ["0", "1"]
    for i in range(1, n):
        rgc = gc[::-1]
        gc = ["0" + i for i in gc] + ["1" + i for i in rgc]
    return gc


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