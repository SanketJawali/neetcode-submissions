class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs(curr: List[int]):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for n in count:
                if count[n] == 0:
                    continue
                curr.append(n)
                count[n] -= 1
                dfs(curr)
                count[n] += 1
                curr.pop()

        dfs([])
        return res