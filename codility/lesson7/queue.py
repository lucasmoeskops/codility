class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.head, self.tail = 0, 0
        self.size = size

    def push(self, x):
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = x

    def pop(self):
        self.head = (self.head + 1) % self.size
        return self.queue[self.head]

    def size(self):
        return (self.tail - self.head + self.size) % self.size()

    def empty(self):
        return self.head == self.tail
