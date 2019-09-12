def solution(A, B):
    # write your code in Python 3.6
    fish_alive = len(A)
    encounter = []

    for fish in range(len(A)):
        if B[fish] == 1:
            encounter.append(fish)
        elif encounter:
            while encounter:
                fish_alive -= 1

                if A[encounter[-1]] < A[fish]:
                    encounter.pop()
                else:
                    break

    return fish_alive
