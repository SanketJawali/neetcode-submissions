class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        a = b = 1
        for b in range(1, len(nums)):
            if nums[b] != nums[b - 1]:  # Found a unique number
                nums[a] = nums[b]
                a += 1
            
        return a