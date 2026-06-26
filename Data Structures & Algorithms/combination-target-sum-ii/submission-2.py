class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Constraints: 
        # - Numbers from input cannot be repeated
        # - Sum of all numbers should be == target

        # For the first constraint, we can choose to have two options on each node
        # 1. We choose the current number to be added in subtree
        # 2. We do not choose to do the same (combinations except the current number)

        result = []
        candidates.sort()

        combination = []
        def dfs(i: int, total: int):
            if total == target:
                result.append(combination.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # Explore combinations with current element
            combination.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            # Explore combinations without current element
            combination.pop()
            # Skip all duplicates, so we avoid adding same combination
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            # if i == len(candidates) - 1 and candidates[i] == candidates[i - 1]:
            #     return
            
            dfs(i + 1, total)

        dfs(0, 0)
        return result