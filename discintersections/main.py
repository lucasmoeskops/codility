from bisect import bisect


def solution(A):
    # write your code in Python 3.6
    impact = []
    pairs = 0
    outdated = 0

    for index, radius in enumerate(A):
        impact.append(index - radius)

    impact = sorted(impact)

    for index, radius in enumerate(A):
        outdated += 1
        pairs += bisect(impact, index + radius) - outdated

        if pairs > 1e7:
            return -1

    return pairs
