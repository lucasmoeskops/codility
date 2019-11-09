from random import randint
from typing import NamedTuple

from max_double_slice_sum.main import solution


class DebugVal(NamedTuple):
    post_pivot_best: int
    pivot: int
    current: int
    maximum: int
    value: int


def brute_force(A):
    """ O(n^3) implementation """
    best_at = 0, 0, 0
    best = 0
    for a in range(len(A) - 2):
        for b in range(a + 1, len(A) - 1):
            for c in range(a + 2, len(A)):
                total = sum(A[a + 1:b]) + sum(A[b + 1:c])
                if total > best:
                    best = total
                    best_at = a, b, c
    return best, best_at


def find():
    """ Find mismatches between O(n) and O(n^3) implementation"""
    b = 0
    q = 0
    while b == q:
        seq = [randint(-10, 10) for _ in range(randint(15, 30))]
        b, b_at = brute_force(seq)
        q = solution(seq)
    print(seq, b, q, b_at)


def test():
    # Tests and mismatches
    seqs = (
        ([3, 2, 6, -1, 4, 5, -1, 2], 17),
        ([0, -1000, 1, 2, -1001, 3, 4], 6),
        ([0, -1000, 1, 2, -999, 3, 4], 6),
        ([0, -1000, 1, 2, -999, -999, 4, 4, 4], 8),
        ([7, 4, 9, -6, 1, 5, -6, -10, 4, -2, -2, 10, 3, 3, 2, 4, 0, 10, -1], 39),
        ([0, -6, 10, 7, 0, 1, 4, -8, -2, 6, 0, -5, 2, 9, -2, -7, 0], 32),
        ([8, -8, -6, -10, 9, -8, 10, 3, 8, -4], 30),
        ([6, -7, 1, 7, -9, -7, 8, -1, -1, 3, -8, -6, -9, -4, -10, 3, 3, 5, 6, 2], 17),
        ([5, -4, 1, -10, -9, 9, 7, 5, -6, 9, 1, -9, -10, 3, -9, -2, 8, 9], 31),
        ([-6, -3, 9, -7, -7, 6, 4, 9, -1, 7, -4, -4, 3, 6, 7], 30),
        (
            [2, -10, -3, 8, 6, -3, 4, -5, 5, -1, -9, -7, 1, -5, 8, 5, -9, 8, -6, -1, 0, 3],
            21
        ),
        ([-2, 10, 8, -6, -3, -2, -5, -4, -4, 8, -5, 8, -1, 6, 4, 8, 3, -4, -1, 5], 36),
        ([8, 8, -9, -2, 1, -4, 3, 7, 9, 9, 5, -8, 5, 9, -4], 47),
        ([6, -9, 3, 4, 2, -7, -4, -10, 4, 6, -9, 1, 7, -1, 3], 18),
        ([-7, -3, 0, -9, -4, 2, -2, 8, -9, 10, -1, 3, 1, -7], 21),
        ([-6, -4, 5, -4, -2, -2, 5, 0, -9], 6),
    )
    for seq, expected in seqs:
        assert solution(seq) == expected, seq
