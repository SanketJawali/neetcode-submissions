class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def twoSum(first, target):
            l, r = first + 1, len(nums) - 1

            while l < r:
                currsum = nums[l] + nums[r]
                if currsum == target:
                    res.append([nums[first], nums[l], nums[r]])
                    l += 1
                    # Avoid finding duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif currsum > target:
                    r -= 1
                else:
                    l += 1

        # Choose first element
        for i in range(len(nums) - 2):
            # There can't be 2 +ve nums with target < 0
            if nums[i] > 0: return res

            # Skip repeated same elements to avoid duplicates'
            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            twoSum(i, -1 * nums[i])
    
        return res