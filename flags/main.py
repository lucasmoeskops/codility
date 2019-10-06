# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import tee
from operator import itemgetter


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def solution(A):
    # write your code in Python 3.6
    peaks = [i for i in range(1, len(A) - 1) if A[i - 1] < A[i] > A[i + 1]]

    if not peaks:
        return 0

    distances = [q - p for p, q in pairwise(peaks)]
    max_flags = len(peaks)

    min_distance = min(distances)
    while min_distance < max_flags:
        max_flags -= 1
        options = []
        for index, distance in enumerate(distances):
            if distance == min_distance:
                if index > 0:
                    options.append((index, distances[index - 1]))
                else:
                    options.append((index, max_flags))
        best_option = min(options, key=itemgetter(1))[0]
        if best_option > 0:
            distances[best_option - 1] += min_distance
        distances[best_option] = max_flags
        min_distance = min(distances)

    return max_flags

