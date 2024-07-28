# Naloga 1: Ničle
# Emina Merlak Susman, 27151132
# praktična matematika, 3. letnik

t = int(input())

def fibonacci_mod(n, m):
    # returns nth fibonacci number modulo m
    pisano_period = pisano(m)
    a = 0
    b = 1

    n = n % pisano_period
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n - 1):
            a, b = b, a + b
        return b % m

def pisano(m):
    # returns length of pisano period modulo m
    a = 0
    b = 1
    for i in range(0, m*m):
        a, b = b, (a + b) % m
        if (a == 0 and b == 1):
            return i + 1
    return b

for j in range(t):
    n, m = map(int, input().split())
    a1 = fibonacci_mod(2 * n - 2 + 2, m)
    a2 = fibonacci_mod(n-2 + 2, m)
    a_n = (a1 - a2) % m
    print(a_n)