from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [2, 3, -1, -4, 2, -5]
        # [-4, -5)
        stack = deque()

        for i in range(len(asteroids)):
            n = asteroids[i]
            while len(stack) > 0:
                if stack[-1] > 0 and n < 0:
                    if abs(stack[-1]) == abs(n):
                        stack.pop()
                        n = None
                        break
                    elif abs(stack[-1]) < abs(n):
                        stack.pop()
                    else:
                        n = None
                        break
                else:
                    stack.append(n)
                    break
            if len(stack) == 0 and n is not None:
                stack.append(n)
        return list(stack)