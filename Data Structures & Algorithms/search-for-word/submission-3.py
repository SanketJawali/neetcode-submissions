class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Assume the word doesn't exists
        res = False

        # Find the first letter of word in board
        potential = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                l = len(board[0])
                if board[i][j] == word[0]:
                    potential.add(self.getIndex(j, i, l))
        print(potential)
        # For all potential starts, try and find the word
        def searchBoard(x, y, term, visited):

            # Check if index within range:
            if not (0 <= x < len(board[0])):
                return False
            if not (0 <= y < len(board)):
                return False

            # If we revisit a cell, we don't know if word exists
            if self.getIndex(x, y, len(board[0])) in visited:
                return False
            # Check only single word term
            if len(term) == 1:
                return board[y][x] == term[0]

            # If first letter in term is board[y][x]
            # Search next letter in top, left, bottom, right
            # Assume word is not there
            left = bottom = right = top = False
            if board[y][x] == term[0]:
                print(f"Found {term[0]} at {self.getIndex(x, y, len(board[0]))}")
                idx = self.getIndex(x, y, len(board[0]))
                visited.add(idx)

                left = searchBoard(x-1, y, term[1:], visited)
                bottom = searchBoard(x, y+1, term[1:], visited)
                right = searchBoard(x+1, y, term[1:], visited)
                top = searchBoard(x, y-1, term[1:], visited)
                
                visited.remove(idx)
            print()
            return left or bottom or right or top

        # For all the potential starts, search the word
        for p in potential:
            x, y = self.getCoordinates(p, len(board[0]))
            print(x, y)
            res = res or searchBoard(x, y, word, set())
        
        return res


    def getIndex(self, x: int, y: int, l: int) -> int:
        """
        Function to get the index of the current cell (x, y).
        """
        return ((y * l) + x + 1)
    

    def getCoordinates(self, idx: int, l: int) -> List[int]:
        """
        Given the index of a letter, get the index
        """
        x = (idx % l) - 1
        if x < 0:
            x += l
        y = (idx - 1) // l
        return [x, y]
