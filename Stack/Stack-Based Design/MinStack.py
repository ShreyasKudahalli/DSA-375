class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min = val
        else:
            if self.min > val:
                self.stack.append(2*val-self.min)
                self.min = val
            else:
                self.stack.append(val)
    
    def pop(self) -> None:
        if not self.stack:
            return -1
        x = self.stack.pop()
        if x < self.min:
            self.min=(2*self.min - x)

    def top(self) -> int:
        if not self.stack:
            return None
        x = self.stack[-1]
        if x < self.min:
            return self.min
        else:
            return x

    def getMin(self) -> int:
        return self.min

