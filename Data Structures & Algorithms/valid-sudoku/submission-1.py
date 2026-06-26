class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            found = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in found:
                    return False
                found.add(cell)

        # Check cols
        for c in range(9):
            found = set()
            for r in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in found:
                    return False
                found.add(cell)
        
        # Check 3x3 grids
        r, c = 0, 0
        for i in range(9):
            print(r, c)
            found = set()
            for i in range(3):
                for j in range(3):
                    cell = board[i + (3 * r)][j + (3 * c)]
                    print(cell, found)
                    if cell == ".":
                        continue
                    if cell in found:
                        print(f"block invalid: {r}, {c}, {i}, {j}")
                        return False
                    found.add(cell)
            r += 1
            if r == 3 and c == 2:
                break
            if r == 3:
                r = 0
                c += 1
        return True
