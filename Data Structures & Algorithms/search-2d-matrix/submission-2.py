class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # 2-D binary search
        # First find which row(list) the element lies in
        # Then find the element in that list
        top, bottom, left, right = 0, m - 1, 0, n - 1

        midy = 0
        while top <= bottom:
            midy = (top + bottom) // 2
            print(top, midy, bottom)
            if target == matrix[midy][left] or target == matrix[midy][right]:
                return True
            elif matrix[midy][left] <= target <= matrix[midy][right]:
                break
            elif target < matrix[midy][left]:
                bottom = midy - 1
            elif target > matrix[midy][left]:
                top = midy + 1
        print()
        while left < right:
            midx = (left + right) // 2
            print(left, midx, right)
            if target == matrix[midy][midx]:
                return True
            elif target < matrix[midy][midx]:
                right = midx - 1
            else:
                left = midx + 1
        
        return False