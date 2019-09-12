def solution(N, A):
    counters = [0] * N
    max_counter = 0  # max value in a counter
    counter_max = 0  # value when "max counter" operation was last called

    for action in A:
        if action == N + 1:
            counter_max = max_counter
        else:
            counters[action - 1] = max(counters[action - 1], counter_max) + 1
            max_counter = max(max_counter, counters[action - 1])

    for n in range(N):
        counters[n] = max(counters[n], counter_max)

    return counters
