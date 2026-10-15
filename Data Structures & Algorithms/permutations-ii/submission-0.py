class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort the input to group duplicates together
        res = []

        def dfs(curr: List[int], select: List[bool]):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if select[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and not select[i - 1]: continue
                select[i] = True
                curr.append(nums[i])
                dfs(curr, select)
                curr.pop()
                select[i] = False

        dfs([], [False] * len(nums))
        return res