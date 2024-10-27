st = input()
prev = st[0]
mx = 0
c = 1
for i in st[1:]:
    if i == prev:
        c += 1
    else:
        mx = max(c, mx)
        prev = i
        c = 1
mx = max(c, mx)
print(mx)
