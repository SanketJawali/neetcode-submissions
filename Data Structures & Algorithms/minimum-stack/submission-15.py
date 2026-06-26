class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minval.append(val)

        self.stack.append(val)
        
        if self.minval[-1] >= val and len(self.stack) > 1:
            self.minval.append(val)
        # print(f"push: {val}, {self.stack}, {self.minval}")



    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.getMin():
            self.minval.pop()
        # print(f"pop: {self.stack}, {self.minval}")


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(f"min: {self.minval[-1]}, {self.stack}, {self.minval}")

        return self.minval[-1]