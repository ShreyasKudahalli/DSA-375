class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.curSize = 0
        self.Stack = []

    def push(self, x: int) -> None:
        if self.curSize < self.maxSize:
            self.Stack.append(x)
            self.curSize += 1

    def pop(self) -> int:
        if self.Stack:
            self.curSize -= 1
            return self.Stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        n = min(self.curSize,k)

        for i in range(n):
            self.Stack[i] += val

