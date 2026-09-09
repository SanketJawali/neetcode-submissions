class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def twoSum(i, j, t):
            l, r = j + 1, len(nums) - 1

            while l < r:
                currsum = nums[l] + nums[r]
                if currsum == t:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif currsum > t:
                    r -= 1
                else:
                    l += 1

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                currsum = nums[i] + nums[j]
                twoSum(i, j, target - currsum)
        
        return res