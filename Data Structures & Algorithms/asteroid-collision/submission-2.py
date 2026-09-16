from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for i in range(len(asteroids)):
            # Get current asteroid
            n = asteroids[i]

            # If stack has elements and the top is moving towards n
            while len(stack) > 0:
                if stack[-1] > 0 and n < 0:
                    # If same size, destroy both
                    if abs(stack[-1]) == abs(n):
                        stack.pop()
                        n = None
                        break
                    # If top smaller, destroy it
                    elif abs(stack[-1]) < abs(n):
                        stack.pop()
                    # Destroy n
                    else:
                        n = None
                        break
                # Not moving closer
                else:
                    stack.append(n)
                    break
            if len(stack) == 0 and n is not None:
                stack.append(n)
        return list(stack)