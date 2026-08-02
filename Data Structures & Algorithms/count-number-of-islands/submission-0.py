class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Track number of islands
        res = 0

        def bfs(i, j, searchlist):
            # Check the whole island starting from current land

            # Set current land to '0', to mark it as seen
            grid[i][j] = '0'

            # Check adjacent land
            # If new land found, add it to search list
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':   # Right
                searchlist.append([i, j + 1])
            if j > 0 and grid[i][j - 1] == '1':   # Left
                searchlist.append([i, j - 1])
            if i + 1 < len(grid) and grid[i + 1][j] == '1':   # Bottom
                searchlist.append([i + 1, j])
            if i > 0 and grid[i - 1][j] == '1':   # Top
                searchlist.append([i - 1, j])
            
            # Use dfs to search for connected land
            # print("Search list for [", i, j, "] | ", searchlist)
            for k in searchlist:
                bfs(k[0], k[1], [])
        
        # Iterate through the whole grid
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == "1":
                    # Count new island
                    res += 1
                    bfs(n, m, [])
        
        return res