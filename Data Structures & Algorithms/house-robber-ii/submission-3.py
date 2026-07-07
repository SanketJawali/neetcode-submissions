# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # We can run our algorithm, once with the first element popped
#         # and second time with the last element popped

#         # The first run lets us visit all the possible solutions in the right half of the decision tree
#         # The second run lets us visit all the possible solutions in the left half of the decision tree
#         # The first run is just like regular robber algorithm
#         # The second run is made to look like regular robber algorithm, by dropping the last element
#         # We drop the last element because we have chosen the first element, and now we cannot choose the last element

#         if len(nums) == 1:
#             return nums[0]
        
#         if len(nums) < 4:
#             return max(nums)
        
#         if len(nums) == 4:
#             return max(nums[0]+nums[2], nums[1]+nums[3])
        
#         res = 0

#         cp1 = cp2 = nums.copy()

#         for i in range(len(nums) - 4):
#             if i == 1:
#                 continue
#             cp1[i + 2] = max(cp1[i + 2], cp1[i] + nums[i + 2])
#             cp1[i + 3] = max(cp1[i + 3], cp1[i] + nums[i + 3])
        
#         res = max(res, cp1[-2], cp1[-3])

#         for i in range(1, len(nums) - 3):
#             if i == 2:
#                 continue
#             cp2[i + 2] = max(cp2[i + 2], cp2[i] + nums[i + 2])
#             cp2[i + 3] = max(cp2[i + 3], cp2[i] + nums[i + 3])
        
#         res = max(res, cp2[-1], cp2[-2])

#         return res

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),
                   self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]