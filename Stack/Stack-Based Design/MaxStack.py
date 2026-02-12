class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack = []
        self.max = float('-inf')
        
    
    def push(self, x):
        # Add an element to the top of Stack
        if not self.stack:
            self.stack.append(x)
            self.max = x
        else:
            if self.max < x:
                self.stack.append(2*x-self.max)
                self.max = x
            else:
                self.stack.append(x)

    
    def pop(self):
        # Remove the top element from the Stack
        if not self.stack:
            return -1
        x = self.stack.pop()
        if x > self.max:
            self.max=(2*self.max - x)
        if not self.stack:
            self.max = float('-inf')
            
    def peek(self):
        # Returns top element of Stack
        if not self.stack:
            return -1
        x = self.stack[-1]
        if x > self.max:
            return self.max
        else:
            return x
        
    
    def isEmpty(self):
        return not self.stack
        
    
    def getMax(self):
        # Finds maximum element of Stack
        if not self.stack:
            return -1
        return self.max
