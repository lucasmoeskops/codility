def fibonnaci(i, fibonacci_store=None, max_size=None):
    pre_calculated = get_fibonnaci_store() if fibonacci_store is None else fibonacci_store

    if len(pre_calculated) > i:
        return pre_calculated[i]

    while len(pre_calculated) <= i:
        if max_size is None:
            pre_calculated.append(pre_calculated[-1] + pre_calculated[-2])
        else:
            pre_calculated.append((pre_calculated[-1] + pre_calculated[-2]) % max_size)

    return pre_calculated[i]


def get_fibonnaci_store():
    return [1, 1]


def fibonacci_gen(max_size=None):
    a = 1
    b = 1

    while True:
        yield a
        yield b
        a = a + b
        b = b + a

        if max_size:
            a %= max_size
            b %= max_size
