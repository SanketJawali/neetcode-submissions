class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        if len(nums) == 0:
            return -1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
             
            if nums[l] <= nums[r]:
                # Sorted array
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                continue
            
            if nums[l] <= nums[m]:
                # l and m in first segment
                if target < nums[m] and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # m and r in second segment
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1