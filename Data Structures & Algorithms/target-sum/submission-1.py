class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = {}
        
        def backtrack(i: int = 0, currsum: int = 0):
            if i == len(nums):
                return 1 if currsum == target else 0
            if (i, currsum) in memo:
                return memo[(i, currsum)]

            memo[(i, currsum)] = (backtrack(i + 1, currsum + nums[i]) + backtrack(i + 1, currsum - nums[i]))
            return memo[(i, currsum)]

        return backtrack()
