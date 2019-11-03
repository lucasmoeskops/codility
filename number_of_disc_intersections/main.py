"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N
non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is
drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs
have at least one common point (assuming that the discs contain their borders).

The figure below [figure-1.png] shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying,
publication or disclosure prohibited.
"""

from bisect import bisect


def solution(A):
    # First we calculate for each disc the lowest index it covers and sort this list of
    # indexes. We can then determine how many discs are covering an area below an index.
    # We call this the (lowest) impact list.
    # Each disc i from A will cover at least i discs from the impact list, namely itself
    # and lower discs. By checking for pairs we will subtract this value i because it
    # denotes itself and discs that have already been checked before. Now we can determine
    # the number of new pairs by checking how many discs beyond i are within its impact
    # area ([index - radius, index + radius]). Because all earlier discs are subtracted
    # anyway and later discs will at least cover the current disc if they match, we don't
    # need to mind the (index - radius) boundary when counting. The sum of pairs is the
    # result
    impact = []
    pairs = 0

    for index, radius in enumerate(A):
        impact.append(index - radius)

    impact = sorted(impact)

    for index, radius in enumerate(A):
        pairs += bisect(impact, index + radius) - index - 1

        if pairs > 1e7:
            return -1

    return pairs
