import sys
sys.setrecursionlimit(100000)
INF = (2 ** 64) + 1
import bisect

def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    tails = [] 
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num) 
        else:
            tails[pos] = num 
        print(num, tails, pos)
    return len(tails)  

    
A = [10, 9, 2, 5, 3, 1, 101, 18]
print(longest_increasing_subsequence(A))