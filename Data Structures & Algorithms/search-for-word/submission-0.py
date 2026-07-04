# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         # Assume the word exists
#         res = True

#         # Find the first letter of word in board
#         potential = set()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 potential.add(self.getIndex(i, j, len(board[0])))

#         # For all potential starts, try and find the word
#         def searchBoard(x, y, term, visited):
#             if x, y in visited:
#                 return
#             if len(term) < 1:
#                 return 
#             if len(term) == 1:
#                 return board[y][x] == term[0]

#             if board[y][x] == term[0]:
#                 visited.add(self.getIndex(x, y))
#                 searchBoard(x-1, y, term[1:], visited)
#                 searchBoard(x, y+1, term[1:], visited)
#                 searchBoard(x+1, y, term[1:], visited)
#                 searchBoard(x, y-1, term[1:], visited)




#     def getIndex(x: int, y: int, l: int) -> int:
#         """
#         Function to get the index of the current cell (x, y).
#         x: x value of the current call
#         y: y value of current cell
#         l: length of list, i.e., max x value
#         """
#         return ((y * l) + x + 1)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False