n = int(input())
lst = []
for i in range(n):
    k = list(map(int, input().split()))
    lst.append(k)
lst = sorted(lst, key = lambda x: x[1])
c = 0
l = 0
i = 0
while i < n:
    if lst[i][0] >= l:
        l = lst[i][1]
        c += 1
    i += 1
print(c)
