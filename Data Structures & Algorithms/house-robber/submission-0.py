class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a, b = 0, 0

        for i in nums:
            maxrob = max(a + i, b)
            a = b
            b = maxrob
        return b
