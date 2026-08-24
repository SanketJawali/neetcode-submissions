class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * (2 * N)

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + N] = n
        
        return ans