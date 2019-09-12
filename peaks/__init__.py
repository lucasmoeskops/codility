# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import tee, chain
from math import sqrt


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def solution(A):
    # write your code in Python 3.6
    peaks = [i for i in range(1, len(A) - 1) if A[i - 1] < A[i] > A[i + 1]]

    best = len(peaks)
    factors = set(chain.from_iterable(
        ((i, len(A) // i)
         for i in range(1, int(sqrt(len(A))) + 1)
         if len(A) % i == 0)))

    for num_blocks in sorted((
            factor for factor in factors if factor <= best),
            reverse=True):
        size = len(A) // num_blocks

        if peaks[0] // size > 0 or peaks[-1] // size < num_blocks - 1:
            continue

        for i, j in pairwise(peaks):
            if j // size - i // size > 1:
                break
        else:
            return num_blocks

    return 0