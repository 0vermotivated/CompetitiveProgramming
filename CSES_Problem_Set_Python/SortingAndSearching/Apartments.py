a, b, k = map(int, input().split())
al = sorted(list(map(int, input().split())))
bl = sorted(list(map(int, input().split())))
 
c = 0
inda = 0
indb = 0
while inda < a and indb < b:
    if abs(al[inda] - bl[indb]) <= k:
        c += 1
        inda += 1
        indb += 1
    elif al[inda] > bl[indb]:
        indb += 1
    else:
        inda += 1
print(c)