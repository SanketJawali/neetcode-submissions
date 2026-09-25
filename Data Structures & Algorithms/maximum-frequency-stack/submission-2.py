class FreqStack:

    def __init__(self):
        # {1: [5, 6, 7], 2: [5, 6], 3: [5]}
        self.stacks = {}
        # {5: 3, 6: 2, 7: 1}
        self.count = {}
        # Mostly equal to len(self.stacks)
        self.maxcount = 0

    def push(self, val: int) -> None:
        valcount = self.count.get(val, 0) + 1   # Get current count of val
        if valcount > self.maxcount:            # If count becomes more than current max
            self.stacks[valcount] = []          # New stack for vals with maxcount freq.
            self.maxcount = valcount            # Update maxcount
        self.count[val] = valcount              # Update val's count
        self.stacks[valcount].append(val)       # Add val to stacks

    def pop(self) -> int:
        maxval = self.stacks[self.maxcount].pop()   # Get value with maxcount freq.
        self.count[maxval] -= 1                     # Decrement count of maxval
        if not self.stacks[self.maxcount]:          # Update maxcount if needed
            del self.stacks[self.maxcount]
            self.maxcount -= 1
        return maxval

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()