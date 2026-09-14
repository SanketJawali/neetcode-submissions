from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        n = len(self.queue)
        for _ in range(n - 1):
            e = self.queue.pop()
            self.queue.appendleft(e)
        return self.queue.pop()

    def top(self) -> int:
        n = len(self.queue)
        top = None
        for i in range(n):
            e = self.queue.pop()
            if i == n - 1:
                top = e
            self.queue.appendleft(e)
        return top

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()