n = int(input())
lst = list(map(int, input().split()))
s1 = sum(lst)
s2 = (n + 1) * (n / 2)
print(int(s2 - s1))