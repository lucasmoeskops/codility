from functools import reduce
from random import randint, random


def is_indifferent(a, b, c, d):
    return a < d and b < c and a < c and b < d


def solution(A, B):
    if len(A) < 2:
        return 0

    prev_swap = False
    index = 1
    sub_index = 0
    swaps = 0
    sub_swaps = 0

    for index in range(index, len(A)):
        j = index - 1
        a, b, c, d = A[index], B[index], A[j], B[j]
        S1, S2 = (B, A) if prev_swap else (A, B)
        prev_swap = False

        if d < a and c < b and c < a and d < b:
            swaps += min(sub_swaps, index - sub_swaps - sub_index)
            sub_swaps = 0
            sub_index = index
            continue

        if a <= S1[j] or b <= S2[j]:
            if a > S2[j] and b > S1[j]:
                prev_swap = True
                sub_swaps += 1
            else:
                return -1

    swaps += min(sub_swaps, index - sub_swaps - sub_index + 1)
    return swaps


# def solutionE(A, B, analyze=False):
#     indifferents = []
#     if len(A) < 2:
#         return 0
#
#     if A[0] < B[1] and B[0] < A[1] and A[0] < A[1] and B[0] < B[1]:
#         return solutionE(A[1:], B[1:], analyze)
#
#     S1 = [(A[0], False)]
#     S2 = [B[0]]
#     index = 1
#
#     for index in range(1, len(A)):
#         future_problems = False
#         future_problems_on_swap = False
#
#         if A[index - 1] < A[index] and B[index - 1] < B[index] and B[index - 1] < A[index] and A[index - 1] < B[index]:
#             if index + 1 == len(A) or A[index] < A[index + 1] and B[index] < B[index + 1] and B[index] < A[index + 1] and A[index] < B[index + 1]:
#                 break
#
#         if index + 1 < len(A):
#             if A[index] >= A[index + 1] or B[index] >= B[index + 1]:
#                 future_problems = True
#                 if analyze:
#                     print('Future problems at', index)
#             if A[index] >= B[index + 1] or B[index] >= A[index + 1]:
#                 future_problems_on_swap = True
#                 if analyze:
#                     print('on swap future problems at', index)
#
#         if A[index] <= S1[index - 1][0] or B[index] <= S2[index - 1]:
#             if A[index] > S2[index - 1] and B[index] > S1[index - 1][0]:
#                 if not future_problems and (future_problems_on_swap and A[index] > S2[index - 1] and B[index] > S1[index - 1][0]):
#                         or (future_problems and A[index] > S2[index - 1] and B[index] > S1[index - 1][0]):
                    # t = S1[-1]
                    # S1[-1] = (S2[-1], not t[1])
                    # S2[-1] = t[0]
                    # S1.append((A[index], False))
                    # S2.append(B[index])
                    # check = index - 1
                # else:
                #     S1.append((B[index], True))
                #     S2.append(A[index])
                #     check = index
                #
                # for index_2 in range(check - 1, -1, -1):
                #     if S1[index_2][0] >= S1[index_2 + 1][0] or S2[index_2] >= S2[index_2 + 1]:
                #         t = S1[index_2]
                #         S1[index_2] = (S2[index_2], not S1[index_2][1])
                #         S2[index_2] = t[0]
                #     else:
                #         break
            # else:
            #     return -1
        # else:
        #     S1.append((A[index], False))
        #     S2.append(B[index])
        #
        #
        # if analyze:
        #     print(S1, S2, indifferents)
    # else:
    #     index += 1
    #
    # swaps = sum(1 for _, swapped in S1 if swapped)
    # indifferents = sum(1 for index in indifferents if not S1[index][1])
    # if A[0] < B[1] and B[0] < A[1] and A[0] < A[1] and B[0] < B[1]:
    #     indifferents += 1
    # print(indifferents)
    # print(index)
    # return min(swaps, index - swaps) + solutionE(A[index:], B[index:], analyze)


# def solution(A, B):
#


from itertools import chain, combinations
def powerset(iterable):

    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def test(A, B):
    for combination in powerset(range(len(A))):
        S1 = [B[i] if i in combination else A[i] for i in range(len(A))]
        S2 = [A[i] if i in combination else B[i] for i in range(len(A))]
        for i in range(len(A) - 1):
            if S1[i] >= S1[i + 1] or S2[i] >= S2[i + 1]:
                break
        else:
            print('Cheapest is ', len(combination), 'with', combination)
            return len(combination)


def gen_sequence(l=8, r=False):
    S1 = list(reduce(lambda p, n: p + [randint(p[-1] + 1, p[-1] + 10)], [0] * l, [randint(0, 5)]))
    S2 = list(reduce(lambda p, n: p + [randint(p[-1] + 1, p[-1] + 10)], [0] * l, [randint(0, 5)]))
    if not r:
        for combination in powerset(range(l)):
            yield [S1[i] if i in combination else S2[i] for i in range(l)], [S2[i] if i in combination else S1[i] for i in range(l)]
    else:

        v = [(S1[i], S2[i]) if random() > 0.5 else (S2[i], S1[i]) for i in range(l)]
        yield [a[0] for a in v], [a[1] for a in v]


def tester(l=8):
    gen = gen_sequence(l)
    def f():
        A, B = next(gen)
        print(A, B)
        s, t = solution(A, B), test(A, B)
        if s != t:
            raise RuntimeError('{}, {}, {}, {}'.format(A, B, s, t))
    while True:
        try:
            f()
        except StopIteration:
            break
