class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occured = []
        for num in nums:
            if num in occured:
                return True
            occured.append(num)
        
        return False