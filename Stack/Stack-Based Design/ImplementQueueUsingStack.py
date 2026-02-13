class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        self.inputStack.append(x)

    def pop(self) -> int:
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
        return self.outputStack.pop() if self.outputStack else -1

    def peek(self) -> int:
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
        return self.outputStack[-1] if self.outputStack else -1

    def empty(self) -> bool:
        if not self.inputStack and not self.outputStack:
            return True
        return False


