class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Track number of islands
        res = 0

        def bfs(i, j):
            adj = [[0, -1], [0, 1], [-1, 0], [1, 0]]

            # Define Queue for BFS
            queue = deque()
            queue.append([i, j])

            while len(queue) > 0:
                l = len(queue)

                for _ in range(l):
                    i, j = queue.popleft()

                    # Check again if [i, j] is land, and is not visited
                    if not grid[i][j] == '1':
                        continue

                    # Mark current land as seen
                    grid[i][j] = '0'

                    # Search adjacent land
                    for d in adj:
                        di, dj = i + d[0], j + d[1]
                        if (
                            0 <= di < len(grid) and 
                            0 <= dj < len(grid[0]) and 
                            grid[di][dj] == '1'
                            ):
                            queue.append([di, dj])\
        
        # Iterate through the whole grid
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == "1":
                    # Count new island
                    res += 1
                    bfs(n, m)
        
        return res