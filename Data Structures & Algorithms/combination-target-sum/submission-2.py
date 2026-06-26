class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # Use backtracking, on each step, choose the one of the numbers form nums
        # Return when sum of current path is > target
        # if sum is == to target, add it to result

        # Brute Force solution
        # combination = []
        # def dfs(total):
        #     if total > target:
        #         return
        #     if total == target:
        #         final = sorted(combination.copy())
        #         if not final in result:
        #             result.append(final)
        #         return
        #     for n in nums:
        #         combination.append(n)
        #         dfs(total + n)
        #         combination.pop()
        # dfs(0)

        # Optimized solution
        combination = []
        def dfs(array, total):
            if total == target:
                result.append(combination.copy())
                return
            if total > target:
                return
            if len(array) < 1:
                return
            
            # Subtree including array[0]
            combination.append(array[0])
            dfs(array, total + array[0])

            # Subtree excluding array[0]
            combination.pop()
            if len(array) > 1:
                dfs(array[1:], total)
        dfs(nums, 0)

        return result