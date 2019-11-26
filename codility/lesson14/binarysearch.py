from typing import Callable


class BinarySearch:
    def __init__(self, checker: Callable, length=None):
        self.checker = checker
        self.length = length

    def __getitem__(self, i):
        return self.checker(i)

    def __len__(self):
        return self.length
