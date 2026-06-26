class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2-D binary search
        # First find which row(list) the element lies in
        # Then find the element in that list
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        midy = 0
        # Search along y-axis
        while top <= bottom:
            midy = (top + bottom) // 2
            # print(top, midy, bottom)

            if matrix[midy][left] <= target <= matrix[midy][right]:
                break
            elif target < matrix[midy][left]:
                bottom = midy - 1
            elif target > matrix[midy][left]:
                top = midy + 1
        # Search in the matrix, i.e., along x-axis
        while left <= right:
            midx = (left + right) // 2
            # print(left, midx, right)
            if target == matrix[midy][midx]:
                return True
            elif target < matrix[midy][midx]:
                right = midx - 1
            else:
                left = midx + 1
        
        return False