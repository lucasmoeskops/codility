# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter


def solution(A):
    # write your code in Python 3.6
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
