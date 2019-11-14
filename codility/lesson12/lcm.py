from math import gcd


def lcm(n, m):
    return n * m // gcd(n, m)
