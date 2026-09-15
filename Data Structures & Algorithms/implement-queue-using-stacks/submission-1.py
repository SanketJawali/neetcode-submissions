from collections import deque

class MyQueue:

    def __init__(self):
        self.s = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        while len(self.s) > 0:
            self.s2.append(self.s.pop())
        self.s.append(x)
        while len(self.s2) > 0:
            self.s.append(self.s2.pop())

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()