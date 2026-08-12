from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        adj = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        queue = deque()

        # Iterate through grid and find chests
        # UPDATE: We remove the call to bfs from the nested loop and 
        # call it after we have found all the treasure chests have been found.
        # This way we have bfs from each chest positions running concurrently
        # Now we don't need to update an already visited land cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    # Removed: bfs()
        
        dist = 0
        def bfs():
            # For each element in the queue, find adjacent land, add land to queue
            while queue:
                l = len(queue)
                for _ in range(l):
                    # Fetch element from queue
                    a, b = queue.popleft()

                    # Update current land value to min distance from chest
                    # NOTE: keep the min() call, this handles the case where a cell
                    # is between two chests
                    nonlocal dist
                    grid[a][b] = min(grid[a][b], dist)

                    # Find land adjacent to grid(a, b)
                    for d in adj:
                        da, db = a + d[0], b + d[1]
                        # Add land to queue
                        if (
                            0 <= da < len(grid) and
                            0 <= db < len(grid[0]) and
                            grid[da][db] == 2147483647
                        ):
                            # Add adjacent land to queue, so it can be visited
                            queue.append([da, db])
                            # Update grid(da, db) to make it as visited and prevent revisits
                            grid[da][db] -= 1
                
                # Add distance from chest
                dist += 1
        bfs()