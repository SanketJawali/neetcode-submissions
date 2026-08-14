class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        # Start from edge cells of one ocean
        # Visit all the cells which can reach this ocean, add these cells to the set
        # Do the same for other ocean
        # The common cells in both sets, are the ones which can reach both the oceans

        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(r, c, oset):
            # r: row, c: col, oset: ocean set, h: height of previous cell
            nonlocal ROWS
            nonlocal COLS
            # Add cell to set
            oset.add((r, c))
            h = heights[r][c]

            # For each adjacent cell, if the height is equal or greater, recursively visit it
            for d in adj:
                dr, dc = r + d[0], c + d[1]
                if (
                    (dr, dc) not in oset and
                    0 <= dr < ROWS and
                    0 <= dc < COLS and
                    heights[dr][dc] >= h
                ):
                    dfs(dr, dc, oset)

        # Start from cells on left and right column
        for c in range(COLS):
            dfs(0, c, pacific)            # Pacific ocean col
            dfs(ROWS - 1, c, atlantic)    # Atlantic ocean col
        
        # Start from cells on top and bottom rows
        for r in range(ROWS):
            dfs(r, 0, pacific)            # Pacific ocean col
            dfs(r, COLS - 1, atlantic)    # Atlantic ocean col

        # Find the common cells in both sets, return them as a list
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                cell = (i, j)
                if cell in pacific and cell in atlantic:
                    res.append([i, j])

        return res