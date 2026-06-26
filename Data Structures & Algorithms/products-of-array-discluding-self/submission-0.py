class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        results = []

        for i in range(len(nums) - 1):
            # Prefix
            if len(prefix) == 0:
                prefix.append(nums[i]) # i = 0
            else:
                prefix.append(prefix[-1] * nums[i])
            
            # Suffix
            if len(suffix) == 0:
                suffix.append(nums[len(nums) - i - 1])
            else:
                suffix.append(suffix[-1] * nums[len(nums) - i - 1])
            
        for i in range(len(nums)):
            left = 1
            right = 1

            if not i == 0:
                left = prefix[i - 1]
            if not i == len(nums) - 1:
                right = suffix[(-1 * i) - 1]

            results.append(left * right)

        return results