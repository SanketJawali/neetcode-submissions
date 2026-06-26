class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(n):
            # Check if leaf node reached
            if n >= len(nums):
                result.append(subset.copy())
                return
            
            # Include the current element
            subset.append(nums[n])
            dfs(n+1)
            # Skip the current element
            subset.pop()
            dfs(n+1)
        dfs(0)

        return result
