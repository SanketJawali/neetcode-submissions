from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minutes = 0

        # Scan grid for rotten fruit sources
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r, c])

        def addFruit(r: int, c: int):
            if (
                0 <= r < len(grid) and
                0 <= c < len(grid[0]) and
                grid[r][c] == 1
            ):
                # Update value of found fruit, to avoid revisits
                grid[r][c] = -1
                queue.append([r, c])

        def bfs():
            while queue:
                l = len(queue)
                for _ in range(l):
                    r, c = queue.popleft()

                    # Rot the fruit
                    grid[r][c] = 2

                    # Find adjacent fruits
                    addFruit(r - 1, c)
                    addFruit(r + 1, c)
                    addFruit(r, c - 1)
                    addFruit(r, c + 1)
                # Break loop before incrementing minutes if queue empty
                # Don't track minutes if all (rechable) fruits rotted
                if len(queue) == 0:
                    break
                nonlocal minutes
                minutes += 1
        bfs()
        
        # Scan grid for any fresh fruits remaining
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        return minutes