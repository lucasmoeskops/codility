"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such
that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at
least two elements). The average of a slice (P, Q) is the sum of
A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the
average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position
of the slice with the minimal average. If there is more than one slice with a minimal
average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

__author__ = 'Lucas Moeskops'


def solution(A):
    total, num = A[0] + A[1], 2
    best = (A[0] + A[1]) / 2
    best_at = 0
    avg = total / num
    for index, value in enumerate(A[2:], start=2):
        # In the first case the value makes our average worse, so we can better
        # stop using it and start a new average. In the second case the value doesn't
        # make our average worse and the previous value already made the average better,
        # so together they form a new sequence with a lower general average
        if value > avg or A[index - 1] <= avg:
            # Start a new sequence
            if avg < best:
                best = avg
                best_at = index - num
            total, num = A[index - 1] + A[index], 2
        else:
            total += A[index]
            num += 1
        avg = total / num

    return len(A) - num if avg < best else best_at

