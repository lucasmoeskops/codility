# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max_sum = A[0]
    current_max = A[0]

    for value in A[1:]:
        current_max = max(current_max + value, value)
        max_sum = max(max_sum, current_max)

    return max_sum
