# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max_profit = 0
    buy = 0
    sell = 0

    while sell < len(A):
        while sell + 1 < len(A) and A[sell + 1] - A[buy] > A[sell] - A[buy]:
            sell += 1

        max_profit = max(max_profit, A[sell] - A[buy])
        if sell + 1 < len(A):
            buy = buy if A[buy] < A[sell + 1] else sell + 1
        sell = sell + 1

    return max_profit


def solution2(A):
    min_ending = A[0]
    max_slice = 0

    for a in A:
        min_ending = min(min_ending, a)
        max_slice = max(max_slice, a - min_ending)

    return max_slice