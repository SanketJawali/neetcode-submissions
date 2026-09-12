class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2, 1, 5, l1, 5, r3] res = 3
    
        # Using a Sliding window
        # Move L when currsum >= target
        # Move R when currsum < target

        res = 0
        l = r = 0
        currsum = nums[r]
        while l <= r < len(nums):
            if currsum >= target:
                # update res
                res = min(res, (r - l + 1)) if res > 0 else (r - l + 1)
                # update ptr
                currsum -= nums[l]
                l += 1
            else:
                r += 1
                currsum += nums[r] if r < len(nums) else 0
        
        return res