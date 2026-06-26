class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = len(nums) // 2
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            print(nums[l], nums[m], nums[r])
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res