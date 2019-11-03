"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if
0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular
triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying,
publication or disclosure prohibited.
"""
from itertools import tee

__author__ = 'Lucas Moeskops'


def solution(A):
    # the best candidates are always as close to each other as possible, therefor sorting
    # is useful
    if len(A) < 3:
        return 0

    values = sorted(A)
    P, Q, R = tee(values, 3)
    next(Q)
    next(R)
    next(R)
    for p, q, r in zip(P, Q, R):
        # r + q > p holds, r + p > q holds, but does p + q > r hold?
        if p + q > r:
            return 1
    return 0
