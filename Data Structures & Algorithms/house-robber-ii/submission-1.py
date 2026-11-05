class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(houses: List[int]):
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 0:
                return 0

            one, two = 0, 0
            for i in range(len(houses)):
                tmp = max(one + houses[i], two)
                one = two
                two = tmp
            return two
        return max(helper(nums[1:]), helper(nums[:-1]))