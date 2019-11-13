def array_F(n):
    F = [0] * (n + 1)
    i = 2
    k = 4
    s = 5

    while k <= n:
        if F[i] == 0:
            m = k
            while m <= n:
                if F[m] == 0:
                    F[m] = i

                m += i

        i += 1
        k += s
        s += 2

    return F


def factorization(x, F):
    prime_factors = []

    while F[x] > 0:
        prime_factors.append(F[x])
        x /= F[x]

    prime_factors.append(x)
    return prime_factors
