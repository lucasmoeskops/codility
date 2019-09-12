# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from math import sqrt


def solution(N):
    # write your code in Python 3.6
    is_sqrt = int(sqrt(N)) ** 2 == N
    return (-1 if is_sqrt else 0) + sum(2 for i in range(1, int(sqrt(N)) + 1) if N % i == 0)

