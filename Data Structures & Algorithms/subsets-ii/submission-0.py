class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Number of subsets: 2^n; n = len(nums)
        # Constraints:
        # - Subset length should be < len(nums)
        # - No element should be repeated in a subset
        # - All subsets in result should be unique
        
        # Main problem
        # Duplicate elements should not result in generating repeated subet
        
        # Approach:
        # We can use a recursive backtracking approach, we can effectively plot a decision tree
        # At each node of the tree, we can choose one element, or not choose it
        # If we decide to choose the current element, we explore all subsets with the element
        # We can use an index i to track current index, and pass next index to the recursive call
        # When we choose not to use the current element,
        # We can skip all the indexes with element that are duplicate of the current element
        # Sorting the input before hand is useful here, it makes it easier to skip elements.

        nums.sort()
        result = []
        subset = []
        
        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # Choose the current element, explore subtree
            subset.append(nums[i])
            backtrack(i+1)
            # Skip the current element, explore subtree
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1)
        backtrack(0)
        return result