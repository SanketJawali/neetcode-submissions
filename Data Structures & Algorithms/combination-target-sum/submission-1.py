class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # Use backtracking, on each step, choose the one of the numbers form nums
        # Return when sum of current path is > target
        # if sum is == to target, add it to result

        combination = []
        def dfs(total):
            if total > target:
                return
            if total == target:
                final = sorted(combination.copy())
                if not final in result:
                    result.append(final)
                return
            for n in nums:
                combination.append(n)
                dfs(total + n)
                combination.pop()
        dfs(0)

        return result