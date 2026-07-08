class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.straightRob(nums[1:]), self.straightRob(nums[:-1]))

    def straightRob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        for n in nums:
            maxRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = maxRob
        return rob2