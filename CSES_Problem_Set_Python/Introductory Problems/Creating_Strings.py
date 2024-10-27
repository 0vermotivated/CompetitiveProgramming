nm = lambda: int(input())
lst = lambda: list(map(int, input().split()))
nmm = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7

def rec(cur, left):
    global words
    if left != "":
        for i in range(len(left)):
            rec(cur + left[i], left[:i] + left[i + 1:])
    else:
        words.add(cur)
words = set()


def solve():
    global words
    s = input()
    rec("", s)
    words = list(words)
    words.sort()
    print(len(words))
    for word in words:
        print(word)




for _ in range(1):
    solve()
