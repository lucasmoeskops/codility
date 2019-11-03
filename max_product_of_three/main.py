"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R)
equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying,
publication or disclosure prohibited.
"""

__author__ = 'Lucas Moeskops'


def solution(A):
    # Keep the three highest values and replace the lower ones if we find higher ones
    triplet_max = A[:3]
    # To account for the possibility of two negative values outmatching similar positive
    # values, also keep track of the two lowest numbers
    duo_min = A[:2]
    worst_best = min(triplet_max)
    best_worst = max(duo_min)
    for index, value in enumerate(A[2:], start=2):
        if value > worst_best and index > 2:
            triplet_max[triplet_max.index(worst_best)] = value
            worst_best = min(triplet_max)
        if value < best_worst:
            duo_min[duo_min.index(best_worst)] = value
            best_worst = max(duo_min)
    # Either the three best values or the two worst values and the best value produce
    # the highest triplet.
    return max(
        triplet_max[0] * triplet_max[1] * triplet_max[2],
        max(triplet_max) * duo_min[0] * duo_min[1]
    )
