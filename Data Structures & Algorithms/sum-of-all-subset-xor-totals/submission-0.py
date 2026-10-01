class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        self.res = 0
        def dfs(i: int, currsum: int):
            if i == len(nums):
                self.res += currsum
                return

            dfs(i + 1, currsum ^ nums[i])
            dfs(i + 1, currsum)
        
        dfs(0, 0)
        return self.res