class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n // 3
        res = set()
        counts = {}

        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
            if counts[n] > limit:
                res.add(n)
        
        return list(res)