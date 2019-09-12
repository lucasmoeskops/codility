def solution(H):
    # write your code in Python 3.6
    stack = []
    blocks = 0
    for height in H:
        while stack and stack[-1] > height:
            stack.pop()

        if stack and stack[-1] == height:
            continue

        stack.append(height)
        blocks += 1

    return blocks
