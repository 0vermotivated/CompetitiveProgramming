import time
from SortingAlgorithms import*
from random import*

def ct(x, arg):
    st = time.time()
    x(arg)
    end = time.time()
    return end - st


lst = [randint(1, 10 ** 4) for i in range(10 ** 4)]
sorts = [selectionsort, mergesort, bubblesort]
for i in sorts:
    print(i(lst))
    print(checktime(i, lst))
