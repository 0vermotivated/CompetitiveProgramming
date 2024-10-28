import math
MOD = 10 ** 9 + 7


def fibonacciFD(n):
    def fib_helper(k):
        if k == 0:
            return (0, 1)
        else:
            a, b = fib_helper(k // 2)
            c = a * ((b << 1) - a)  # F(2k) = F(k) * (2*F(k+1) - F(k))
            d = a * a + b * b  # F(2k+1) = F(k+1)^2 + F(k)^2
            if k % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    return fib_helper(n)[0]


def FastPow(x,k):
    res = 1
    while k:
        if k & 1:
            res = res * x % MOD
        x=x*x%MOD
        k>>=1
    return res


def SumToN(n):
    return (n * (n - 1)) // 2


def SqSumToN(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


