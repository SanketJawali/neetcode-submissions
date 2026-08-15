class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Find all 'O' at the edge of board
        # Find Region which is connected to these cells
        # Add the cells of these regions to a set
        # Iterate through board and any cell that has 'O' and is not in the set, is replaced

        ROWS, COLS = len(board), len(board[0])
        o, x = 'O', 'X'
        edgeregion = set()
        
        def dfs(r, c):
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                board[r][c] != o or
                (r, c) in edgeregion
            ):
                return

            edgeregion.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Scan columns for 'O'
        for r in range(ROWS):
            dfs(r, 0)           # Top row
            dfs(r, COLS - 1)    # Bottom row

        # Scan rows for 'O'
        for c in range(COLS):
            dfs(0, c)           # Left col
            dfs(ROWS - 1, c)    # Right col
        
        # Replace enclosed 'O'
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == o and (i, j) not in edgeregion:
                    board[i][j] = x
        