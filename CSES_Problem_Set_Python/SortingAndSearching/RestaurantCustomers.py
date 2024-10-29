n = int(input())
l1 = []
l2 = []
for i in range(n):
    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)
 
l1 = sorted(l1)
l2 = sorted(l2)
i1 = 0
i2 = 0
c = 0
mx = 0
while i1 < n and i2 < n:
    if l1[i1] < l2[i2]:
        i1 += 1
        c += 1
    else:
        i2 += 1
        c -= 1
    mx = max(c, mx)
print(mx)
