from MathFuncs import*
import time
from OtherFuncs import*
from SortingAlgorithms import*
from random import*
import sys
sys.setrecursionlimit(10000)

def ct(x, arg):
    st = time.time()
    x(arg)
    end = time.time()
    return end - st

lst = [randint(-10000000, 10000000) for i in range(5000000)]
print(ct(sorted, lst))
#print(ct(mergesort, lst))