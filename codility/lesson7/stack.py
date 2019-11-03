class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.size = 0

    def __bool__(self):
        return bool(self.size)

    def push(self, x):
        self.stack[self.size] = x
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack[self.size]

    def top(self):
        return self.stack[self.size - 1]
