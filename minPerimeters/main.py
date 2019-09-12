# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from math import sqrt


def solution(N):
    # write your code in Python 3.6
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return 2 * (i + N // i)
