from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def bfs(i, j):
            adj = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            currentArea = 0

            # Define Queue for BFS
            queue = deque()
            queue.append([i, j])

            while len(queue) > 0:
                l = len(queue)

                for _ in range(l):
                    # print(f"Queue: {queue}")
                    i, j = queue.popleft()

                    # Check again if [i, j] is land, and is not visited
                    if not grid[i][j] == 1:
                        continue

                    # Mark current land as seen
                    grid[i][j] = 0
                    currentArea += 1
                    # print(f"Counting {i}, {j}")

                    # Search adjacent land
                    for d in adj:
                        di, dj = i + d[0], j + d[1]
                        if (
                            0 <= di < len(grid) and 
                            0 <= dj < len(grid[0]) and 
                            grid[di][dj] == 1
                            ):
                            queue.append([di, dj])
            
            return currentArea
            
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == 1:
                    res = max(res, bfs(n, m))
        
        return res