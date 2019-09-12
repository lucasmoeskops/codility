# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    matches = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    for char in S:
        if char in matches:
            stack.append(char)
        else:
            try:
                match = stack.pop()
            except IndexError:
                return 0

            if matches[match] != char:
                return 0

    return 1 if not stack else 0
