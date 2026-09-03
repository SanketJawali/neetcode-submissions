class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        # Create a new matrix with 0 padding on top and left side
        # Each cell(r, c) contains sum of all elements from (0, 0) to (r, c)
        self.index = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for r in range(len(self.matrix)):
            prefix = 0
            for c in range(len(self.matrix[0])):
                prefix += matrix[r][c]
                top = self.index[r][c + 1]
                self.index[r + 1][c + 1] = prefix + top
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return self.index[row2][col2] - self.index[row1 - 1][col2] - self.index[row2][col1 - 1] + self.index[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)