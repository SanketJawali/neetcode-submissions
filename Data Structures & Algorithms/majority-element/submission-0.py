from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        maxcount = 0
        
        for n in nums:
            count[n] += 1
            if maxcount < count[n]:
                res = n
                maxcount = count[n]
        
        return res