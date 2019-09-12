from collections import Counter


def solution(A):
    # write your code in Python 3.6
    counter = Counter()
    limit = len(A) // 2

    for index, value in enumerate(A):
        counter[value] += 1

        if counter[value] > limit:
            return index

    return -1