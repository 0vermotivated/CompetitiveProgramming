from MathFuncs import*
import time
from OtherFuncs import*
from SortingAlgorithms import*
from random import*

def ct(x, arg):
    st = time.time()
    x(arg)
    end = time.time()
    return end - st

l = [randint(-100, 100) for i in range(20000000)]
print(ct(BestSubstringSum, l))