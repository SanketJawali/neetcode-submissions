class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = nums[0]

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

            if count[n] > count[majority]:
                majority = n

        return majority