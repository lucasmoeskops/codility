"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences
A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same
value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi
leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying,
publication or disclosure prohibited.
"""

from collections import Counter

__author__ = 'Lucas Moeskops'


def solution(A):
    counter = Counter()

    for value in A:
        counter[value] += 1

    leader, num_leaders = counter.most_common(1)[0]

    left_leaders = 0
    num_equi_leaders = 0

    for index, value in enumerate(A):
        if value == leader:
            left_leaders += 1

        leads_left = left_leaders > (index + 1) // 2
        leads_right = (num_leaders - left_leaders) > (len(A) - index - 1) // 2

        if leads_left and leads_right:
            num_equi_leaders += 1

    return num_equi_leaders
