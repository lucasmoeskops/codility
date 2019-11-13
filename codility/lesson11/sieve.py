def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    k = 4
    s = 5

    while k <= n:
        if sieve[i]:
            while k <= n:
                sieve[k] = False
                k += i

        i += 1
        k += s
        s += 2

    return sieve
