class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        ans = 0

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if self.stack:
            ans =  self.index-self.stack[-1][1]
        else:
            ans = self.index-(-1)
        self.stack.append((price,self.index))
        return ans

